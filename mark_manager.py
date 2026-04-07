"""
@file    mark_manager.py
@author  Rob Pellegrin
@date    02-17-2026

@updated 04-06-2026

"""

import json
from pathlib import Path
from typing import Iterator


class MarkManager:
    _FILE_PATH = Path.home() / ".marks"
    _dirs: list[str]

    # ANSI colors for alternating lines
    COLOR1 = "\033[94m"  # bright blue
    COLOR2 = "\033[96m"  # bright cyan
    RESET = "\033[0m"

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
            idx = int(index)
        except ValueError as e:
            raise ValueError(f"Index must be an integer: {index}") from e

        try:
            print(f"Removed {self._dirs[idx]}")
            self._dirs.pop(idx)
        except IndexError:
            print(f"Index out of range: {index}")
            return

        self._save()

    def get(self, index: str) -> str:
        if index is None and self._dirs:
            return self._dirs[0]

        try:
            return self._dirs[int(index)]
        except (IndexError, ValueError) as e:
            raise ValueError(f"Invalid index: {index}") from e

    def print_dirs(self) -> None:
        for index, directory in enumerate(self):
            print(
                f"{self.COLOR1 if index % 2 else self.COLOR2}"
                f"{' ' * 4}{index}{' ' * 4}{directory}{self.RESET}"
            )

    def clear(self) -> None:
        try:
            Path(self._FILE_PATH).unlink(missing_ok=True)
        except PermissionError as e:
            print(e)

    def __iter__(self) -> Iterator[str]:
        return iter(self._dirs)
