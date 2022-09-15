from __future__ import annotations
from typing import Protocol


class View(Protocol):
    def display_title(self, text: str) -> None:
        ...

    def display_message(self, message: str) -> None:
        ...


class ViewRateZahl:
    def display_title(self, text: str) -> None:
        print(text)

    def display_message(self, message):
        print(message)
