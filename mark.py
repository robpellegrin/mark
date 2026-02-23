"""
@file    mark.py
@author  Rob Pellegrin
@date    02-17-2026

@updated 02-23-2026

"""

import json
import sys
from pathlib import Path
from typing import Iterator

# ANSI colors for alternating lines
COLOR1 = "\033[94m"  # bright blue
COLOR2 = "\033[96m"  # bright cyan
RESET = "\033[0m"


class MarkManager:
    _FILE_PATH = Path.home() / ".marks"
    _dirs: list[str]

    def __init__(self):
        self._load()

    def _load(self) -> None:
        if not self._FILE_PATH.exists():
            self._dirs = []
            return

        with open(self._FILE_PATH, "r", encoding="UTF-8") as f:
            try:
                self._dirs = json.load(f)
            except json.JSONDecodeError:
                print("warning: error decoding JSON file")
                self._dirs = []

    def _save(self) -> None:
        with open(self._FILE_PATH, "w", encoding="UTF-8") as f:
            json.dump(self._dirs, f)

    def add(self, directory: str) -> None:
        directory = str(Path(directory).resolve())

        if directory in self._dirs:
            self._dirs.remove(directory)

        self._dirs.insert(0, directory)
        self._save()

    def remove(self, index: str) -> None:
        try:
            self._dirs.pop(int(index))
            self._save()
        except (IndexError, ValueError) as e:
            raise ValueError(f"Invalid index: {index}") from e

    def get(self, index: str) -> str:
        if index is None and self._dirs:
            return self._dirs[0]

        try:
            return self._dirs[int(index)]
        except (IndexError, ValueError) as e:
            raise ValueError(f"Invalid index: {index}") from e

    def print_dirs(self) -> None:
        for index, directory in enumerate(self):
            print(f"{COLOR1 if index % 2 else COLOR2}" f"{index}\t{directory}{RESET}")

    def clear(self) -> None:
        try:
            Path(self._FILE_PATH).unlink(missing_ok=True)
        except PermissionError as e:
            print(e)

    def __iter__(self) -> Iterator:
        return iter(self._dirs)


def main():
    USAGE = """
Usage:
  mark add [DIR]       Add current or specified directory
  mark list            Show bookmarks
  mark go <NUM>        Print path to change directory to
  mark remove <NUM>    Remove bookmark by number
  mark clear           Delete all bookmarks
"""
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

    print(USAGE)


if __name__ == "__main__":
    main()
