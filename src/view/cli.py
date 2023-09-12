from __future__ import annotations

import abc

from src.mediator import BaseComponent


class View(BaseComponent, abc.ABC):
    def show(self, msg: str) -> None:
        ...

    def get_user_input(self) -> None:
        ...


class CLI(View):
    def show(self, msg: str) -> None:
        print(msg)

    def get_user_input(self) -> None:
        while True:
            self.show("Guess the number: ")
            try:
                result = int(input())
            except ValueError:
                self.show("Please enter a number")
                continue
            else:
                break
        self.mediator.notify(self, result)
