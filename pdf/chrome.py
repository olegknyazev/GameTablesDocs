"""Prints local web pages to PDF with headless Google Chrome, driven over the DevTools protocol."""

import base64
import contextlib
import itertools
import json
import os
import select
import subprocess
import tempfile
from pathlib import Path

DEFAULT_EXECUTABLE = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
RESPONSE_TIMEOUT_SECONDS = 60

# With --remote-debugging-pipe, Chrome reads DevTools commands from fd 3 and writes responses to fd 4.
COMMAND_FD = 3
RESPONSE_FD = 4


def print_to_pdf(executable, html_file: Path, pdf_file: Path, ready_expression):
    """Opens `html_file`, waits until the promise `ready_expression` resolves and saves the page as `pdf_file`."""
    with _running_chrome(executable) as chrome:
        tab = chrome.open_tab(html_file.resolve().as_uri())
        tab.wait_for(ready_expression)
        pdf_file.write_bytes(tab.print_to_pdf())


@contextlib.contextmanager
def _running_chrome(executable):
    with tempfile.TemporaryDirectory() as profile_directory:
        process, command_pipe, response_pipe = _launch(executable, profile_directory)
        with command_pipe, response_pipe:
            try:
                yield Chrome(command_pipe, response_pipe)
            finally:
                process.terminate()
                process.wait()


def _launch(executable, profile_directory):
    command_reader, command_writer = os.pipe()
    response_reader, response_writer = os.pipe()

    def connect_devtools_pipe():
        os.dup2(command_reader, COMMAND_FD)
        os.dup2(response_writer, RESPONSE_FD)

    process = subprocess.Popen(
        [
            executable,
            "--headless",
            "--remote-debugging-pipe",
            "--no-first-run",
            f"--user-data-dir={profile_directory}",
        ],
        pass_fds=(COMMAND_FD, RESPONSE_FD),
        preexec_fn=connect_devtools_pipe,
        stderr=subprocess.DEVNULL,
    )
    os.close(command_reader)
    os.close(response_writer)
    return process, os.fdopen(command_writer, "wb"), os.fdopen(response_reader, "rb", buffering=0)


class DevToolsError(RuntimeError):
    pass


class Chrome:
    """A DevTools protocol connection to a running Chrome."""

    def __init__(self, command_pipe, response_pipe):
        self.command_pipe = command_pipe
        self.response_pipe = response_pipe
        self.message_ids = itertools.count(1)
        self.unread = b""
        self.events = []

    def open_tab(self, url):
        target = self.call("Target.createTarget", url="about:blank")
        session = self.call("Target.attachToTarget", targetId=target["targetId"], flatten=True)
        tab = Tab(self, session["sessionId"])
        tab.navigate(url)
        return tab

    def call(self, method, session_id=None, **params):
        message_id = next(self.message_ids)
        self._send(message_id, method, session_id, params)
        while (message := self._receive()).get("id") != message_id:
            self.events.append(message)
        if "error" in message:
            raise DevToolsError(f"{method} failed: {message['error']['message']}")
        return message["result"]

    def wait_for_event(self, method, session_id):
        def is_awaited(event):
            return event.get("method") == method and event.get("sessionId") == session_id

        while not any(is_awaited(event) for event in self.events):
            self.events.append(self._receive())
        self.events = [event for event in self.events if not is_awaited(event)]

    def _send(self, message_id, method, session_id, params):
        message = {"id": message_id, "method": method, "params": params}
        if session_id:
            message["sessionId"] = session_id
        self.command_pipe.write(json.dumps(message).encode() + b"\0")
        self.command_pipe.flush()

    def _receive(self):
        while b"\0" not in self.unread:
            self.unread += self._read_chunk()
        message, self.unread = self.unread.split(b"\0", 1)
        return json.loads(message)

    def _read_chunk(self):
        readable, _, _ = select.select([self.response_pipe], [], [], RESPONSE_TIMEOUT_SECONDS)
        if not readable:
            raise TimeoutError(f"Chrome did not respond within {RESPONSE_TIMEOUT_SECONDS} seconds")
        chunk = os.read(self.response_pipe.fileno(), 1 << 16)
        if not chunk:
            raise DevToolsError("Chrome closed the DevTools pipe")
        return chunk


class Tab:
    def __init__(self, chrome, session_id):
        self.chrome = chrome
        self.session_id = session_id

    def call(self, method, **params):
        return self.chrome.call(method, self.session_id, **params)

    def navigate(self, url):
        self.call("Page.enable")
        navigation = self.call("Page.navigate", url=url)
        if "errorText" in navigation:
            raise DevToolsError(f"Cannot open {url}: {navigation['errorText']}")
        self.chrome.wait_for_event("Page.loadEventFired", self.session_id)

    def wait_for(self, ready_expression):
        try:
            evaluation = self.call("Runtime.evaluate", expression=ready_expression, awaitPromise=True)
        except TimeoutError:
            message = f"{ready_expression} did not resolve within {RESPONSE_TIMEOUT_SECONDS} seconds"
            raise TimeoutError(message) from None
        if "exceptionDetails" in evaluation:
            raise DevToolsError(f"{ready_expression} failed: {evaluation['exceptionDetails']['text']}")

    def print_to_pdf(self):
        pdf = self.call(
            "Page.printToPDF",
            printBackground=True,
            preferCSSPageSize=True,
            generateTaggedPDF=True,
            generateDocumentOutline=True,
        )
        return base64.b64decode(pdf["data"])
