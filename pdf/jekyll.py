"""Builds the documentation site with Jekyll in the repository's Docker Compose service."""

import subprocess
from pathlib import Path

SITE_IN_CONTAINER = "/site"


def build_site(docs_root: Path, destination: Path):
    """Builds the site into `destination` and returns it."""
    destination.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [
            "docker",
            "compose",
            "run",
            "--rm",
            "--build",
            f"--volume={destination}:{SITE_IN_CONTAINER}",
            "jekyll",
            "jekyll",
            "build",
            # The image's jekyll wrapper breaks options written as --name=value.
            "--destination",
            SITE_IN_CONTAINER,
        ],
        cwd=docs_root,
        check=True,
    )
    return destination
