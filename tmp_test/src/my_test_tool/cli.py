#!/usr/bin/env python3
"""CLI entry point for my_test_tool."""

import argparse
import sys
from typing import NoReturn

from my_test_tool import __version__

__author__ = "John Ayers"


def file_info() -> dict[str, str]:
    """Return module metadata."""
    return {
        "name": "cli",
        "description": "CLI entry point",
        "version": __version__,
        "author": __author__,
        "last_updated": "2025-12-20",
    }


def create_parser() -> argparse.ArgumentParser:
    """Create and configure the argument parser."""
    parser = argparse.ArgumentParser(
        prog="my-test-tool",
        description="A test CLI tool",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose output",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without executing",
    )

    # Add subcommands here
    # subparsers = parser.add_subparsers(dest="command", required=True)

    return parser


def main() -> NoReturn:
    """Main entry point."""
    parser = create_parser()
    args = parser.parse_args()

    # TODO: Implement command handling
    print(f"my-test-tool v{__version__}")
    print("Ready to implement!")

    sys.exit(0)


if __name__ == "__main__":
    main()
