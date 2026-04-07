"""
@file:    main.py
@author:  Rob Pellegrin
@date:    04-06-2026

@updated: 04-06-2026

"""

from cli import process_cli_args
from mark_manager import MarkManager


def main() -> None:
    mark = MarkManager()

    args = process_cli_args()

    if args.add:
        mark.add(args.add)

    if args.go_to is not None:
        if dir_to_go := mark.get(args.go_to):
            print(dir_to_go)
            return

    if args.remove is not None:
        mark.remove(args.remove)

    if args.list:
        mark.print_dirs()


if __name__ == "__main__":
    main()
