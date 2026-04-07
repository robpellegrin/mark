"""
@file:    cli.py
@author:  Rob Pellegrin
@date:    04-06-2026

@updated: 04-06-2026

"""

import argparse
from pathlib import Path


def valid_path(path_str: str) -> Path | None:
    path = Path(path_str)

    if not path.exists():
        return None

    return path


def process_cli_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="marks")

    parser.add_argument(
        "index", nargs="?", type=str, help="position in list"
    )
    parser.add_argument(
        "-a", "--add", type=valid_path, help="add a new path"
    )
    parser.add_argument(
        "-d", "--remove", type=int, help="remove an item by index"
    )
    parser.add_argument(
        "-g", "--go-to", type=int, help="go to (cd) path at index"
    )
    parser.add_argument(
        "-l", "--list", default=True, help="list all entries"
    )

    args = parser.parse_args()

    if args.index:
        try:
            index = int(args.index)
            if args.index.startswith("-"):
                args.remove = abs(index)
            else:
                args.go_to = index
        except ValueError:
            if Path(args.index).exists():
                args.add = Path(args.index)

    return args
