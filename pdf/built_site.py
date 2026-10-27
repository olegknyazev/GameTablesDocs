"""Pages of the documentation site as built by Jekyll with the Just the Docs theme."""

from dataclasses import dataclass
from pathlib import Path

import html_tree


@dataclass
class Page:
    url: str
    depth: int
    content: html_tree.Element


class BuiltSite:
    def __init__(self, root: Path):
        self.root = root.resolve()
        if not self._path("/").is_file():
            raise FileNotFoundError(f"No built site found in {self.root}. Build the site with Jekyll first.")

    def pages(self):
        """Returns the pages in the order of the sidebar navigation."""
        return [Page(url, depth, self._content(url)) for url, depth in self._navigation()]

    def domain(self):
        return (self.root / "CNAME").read_text(encoding="utf-8").strip()

    def package_version(self):
        label = self._parse("/").find("div", "site-version")
        version = label.attributes.get("data-package-version") if label else None
        if not version:
            raise ValueError("The built site has no package version. Set package_version in _config.yml.")
        return version

    def stylesheet(self):
        return (self.root / "assets/css/just-the-docs-default.css").read_text(encoding="utf-8")

    def file_uri(self, url):
        return self._path(url).as_uri()

    def _navigation(self):
        sidebar = self._parse("/").find("nav", "site-nav")
        return list(_navigation_entries(sidebar.child("ul"), depth=0))

    def _content(self, url):
        return self._parse(url).find("main")

    def _parse(self, url):
        return html_tree.parse(self._path(url).read_text(encoding="utf-8"))

    def _path(self, url):
        path = self.root / url.lstrip("/")
        return path / "index.html" if url.endswith("/") else path


def _navigation_entries(navigation_list, depth):
    for item in navigation_list.child_elements():
        yield item.child("a").attributes["href"], depth
        sublist = item.child("ul")
        if sublist:
            yield from _navigation_entries(sublist, depth + 1)
