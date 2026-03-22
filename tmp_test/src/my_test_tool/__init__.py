#!/usr/bin/env python3
"""A test CLI tool"""

__version__ = "0.1.0"
__author__ = "John Ayers"


def file_info() -> dict[str, str]:
    """Return module metadata."""
    return {
        "name": "my_test_tool",
        "description": "A test CLI tool",
        "version": __version__,
        "author": __author__,
        "last_updated": "2025-12-20",
    }
