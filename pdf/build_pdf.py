#!/usr/bin/env python3
"""Builds the documentation site with Jekyll and prints it as a PDF manual."""

import argparse
import tempfile
from pathlib import Path

import chrome
import jekyll
import manual
from built_site import BuiltSite

DOCS_ROOT = Path(__file__).resolve().parent.parent


def main():
    arguments = parse_arguments()
    with tempfile.TemporaryDirectory() as temporary_directory:
        working_directory = Path(temporary_directory)
        site_root = arguments.site or jekyll.build_site(DOCS_ROOT, working_directory / "site")
        html = manual.assemble(BuiltSite(site_root))
        html_file = arguments.html or working_directory / "manual.html"
        html_file.write_text(html, encoding="utf-8")
        chrome.print_to_pdf(arguments.chrome, html_file, arguments.output, manual.LAYOUT_FINISHED)
    print(f"Wrote {arguments.output}")


def parse_arguments():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, help="where to save the PDF")
    parser.add_argument("--site", type=Path, help="use this built site instead of building one with Jekyll")
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
