from __future__ import annotations
from typing import Protocol


class View(Protocol):
    def display_message(self, message: str) -> None:
        ...


class CLI:
    def display_message(self, message: str):
        print(message)
