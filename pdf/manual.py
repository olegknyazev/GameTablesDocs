"""Combines the pages of the built site into a single print-ready HTML document laid out by Paged.js."""

from html import escape
from pathlib import Path
from string import Template

from html_tree import Element

HERE = Path(__file__).parent
TEMPLATE = HERE / "template.html"
PRINT_STYLESHEET = HERE / "print.css"
PAGED_JS = HERE / "vendor" / "paged.polyfill.js"

LAYOUT_FINISHED = "window.layoutFinished"
HEADING_TAGS = ("h1", "h2", "h3", "h4", "h5", "h6")
NUMBERED_LEVELS = 3
CONTENTS_LEVELS = 2


def assemble(site):
    pages = site.pages()
    anchors = Anchors(site.domain(), [page.url for page in pages])
    sections = [to_section(page, site, anchors) for page in pages]
    headings = find_headings(*sections, max_level=NUMBERED_LEVELS)
    add_section_numbers(headings)
    return render(site, table_of_contents(headings), sections)


def to_section(page, site, anchors):
    content = page.content
    remove_heading_links(content)
    remove_child_page_index(content)
    nest_headings(content, page.depth)
    namespace_ids(content, page.url, anchors)
    rewrite_links(content, page.url, anchors)
    point_images_to_files(content, site)
    attributes = {"id": anchors.for_page(page.url), "class": f"page depth-{page.depth}"}
    return Element("section", attributes, content.children)


def remove_heading_links(content):
    """Removes the link icons that the theme puts next to headings."""
    content.remove_descendants("a", "anchor-heading")


def remove_child_page_index(content):
    """Removes the list of child pages that the theme appends to parent pages."""
    elements = content.child_elements()
    for index, element in enumerate(elements):
        if element.matches("h2", "text-delta"):
            separator, heading, page_list = elements[index - 1 : index + 2]
            content.remove(separator, heading, page_list)


def nest_headings(content, depth):
    """Renumbers heading levels to start right below `depth` with no gaps between levels."""
    headings = find_headings(content)
    levels = sorted({heading_level(heading) for heading in headings})
    new_levels = {level: min(depth + rank, 6) for rank, level in enumerate(levels, start=1)}
    for heading in headings:
        heading.tag = f"h{new_levels[heading_level(heading)]}"


def namespace_ids(content, page_url, anchors):
    for element in content.descendants():
        if "id" in element.attributes:
            element.attributes["id"] = anchors.for_element(page_url, element.attributes["id"])


def rewrite_links(content, page_url, anchors):
    for link in content.find_all("a"):
        if "href" in link.attributes:
            link.attributes["href"] = anchors.resolve(link.attributes["href"], page_url)


def point_images_to_files(content, site):
    for image in content.find_all("img"):
        if image.attributes["src"].startswith("/"):
            image.attributes["src"] = site.file_uri(image.attributes["src"])


def add_section_numbers(headings):
    numbers = SectionNumbers(NUMBERED_LEVELS)
    for heading in headings:
        label_heading(heading, numbers.next(heading_level(heading)))


def label_heading(heading, number):
    heading.strip_whitespace()
    number_label = span("section-number", number + "\N{NO-BREAK SPACE}")
    title = span("section-title", *heading.children)
    heading.children = [number_label, title]


def table_of_contents(headings):
    return [contents_entry(heading) for heading in headings if heading_level(heading) <= CONTENTS_LEVELS]


def contents_entry(heading):
    number = heading.find("span", "section-number").text()
    title = heading.find("span", "section-title").text()
    link = Element("a", {"href": "#" + heading.attributes["id"]}, [span("section-number", number), title])
    return Element("li", {"class": f"contents-level-{heading_level(heading)}"}, [link])


def render(site, contents, sections):
    template = Template(TEMPLATE.read_text(encoding="utf-8"))
    return template.substitute(
        site_stylesheet=site.stylesheet(),
        print_stylesheet=PRINT_STYLESHEET.read_text(encoding="utf-8"),
        layout_finished=LAYOUT_FINISHED,
        paged_js=PAGED_JS.as_uri(),
        logo=site.file_uri("/icon.png"),
        package_version=escape(site.package_version()),
        domain=escape(site.domain()),
        contents=to_html(contents),
        sections=to_html(sections),
    )


def find_headings(*roots, max_level=6):
    elements = (element for root in roots for element in root.descendants())
    return [element for element in elements if element.tag in HEADING_TAGS and heading_level(element) <= max_level]


def heading_level(heading):
    return int(heading.tag[1])


def span(class_name, *children):
    return Element("span", {"class": class_name}, children)


def to_html(elements):
    return "".join(element.to_html() for element in elements)


class Anchors:
    """Maps links between site pages to anchors within the single-document manual."""

    def __init__(self, domain, page_urls):
        self.site_url = f"https://{domain}"
        self.page_urls = set(page_urls)

    def for_page(self, url):
        return url.strip("/").removesuffix(".html").replace("/", "-") or "index"

    def for_element(self, page_url, element_id):
        return f"{self.for_page(page_url)}--{element_id}"

    def resolve(self, href, page_url):
        url, _, fragment = href.partition("#")
        url = url or page_url
        if not url.startswith("/"):
            return href
        if url not in self.page_urls:
            return self.site_url + href
        return "#" + (self.for_element(url, fragment) if fragment else self.for_page(url))


class SectionNumbers:
    """Hierarchical section numbers such as 2, 2.1 and 2.1.3."""

    def __init__(self, levels):
        self.counters = [0] * levels

    def next(self, level):
        self.counters[level - 1] += 1
        self.counters[level:] = [0] * (len(self.counters) - level)
        return ".".join(str(counter) for counter in self.counters[:level])
