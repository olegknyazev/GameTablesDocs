#!/usr/bin/env python3
"""Builds the PDF manual from the documentation site built by Jekyll."""

import argparse
import tempfile
from pathlib import Path

import chrome
import manual
from built_site import BuiltSite

DOCS_ROOT = Path(__file__).resolve().parent.parent
PACKAGE_VERSION = "1.0.0"


def main():
    arguments = parse_arguments()
    html = manual.assemble(BuiltSite(arguments.site), PACKAGE_VERSION)
    with tempfile.TemporaryDirectory() as temporary_directory:
        html_file = arguments.html or Path(temporary_directory) / "manual.html"
        html_file.write_text(html, encoding="utf-8")
        chrome.print_to_pdf(arguments.chrome, html_file, arguments.output, manual.LAYOUT_FINISHED)
    print(f"Wrote {arguments.output}")


def parse_arguments():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, help="where to save the PDF")
    parser.add_argument(
        "--site",
        type=Path,
        default=DOCS_ROOT / "_site",
        help="the built site (default: %(default)s)",
    )
    parser.add_argument(
        "--chrome",
        default=chrome.DEFAULT_EXECUTABLE,
        help="the Chrome executable (default: %(default)s)",
    )
    parser.add_argument(
        "--html",
        type=Path,
        help="also save the HTML the PDF is printed from; open it in Chrome to preview the layout",
    )
    return parser.parse_args()


if __name__ == "__main__":
    main()
