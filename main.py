"""
@file:    main.py
@author:  Rob Pellegrin
@date:    04-06-2026

@updated: 04-06-2026

"""

import sys

from mark import MarkManager


def main():
    mark = MarkManager()

    cmd = sys.argv[1] if len(sys.argv) > 1 else "list"
    arg = sys.argv[2] if len(sys.argv) > 2 else None

    if cmd == "add":
        mark.add(arg or str(Path.cwd()))
        return

    if cmd == "list":
        mark.print_dirs()
        return

    if cmd == "go":
        dir_to_go = mark.get(index=arg)

        if dir_to_go:
            print(dir_to_go)
        return

    if cmd == "remove":
        mark.remove(arg)
        return

    if cmd == "clear":
        mark.clear()
        return


if __name__ == "__main__":
    main()
