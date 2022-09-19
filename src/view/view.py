from __future__ import annotations
from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from ..controller.controller import Controller


class View(Protocol):
    def display_message(self, message: str) -> None:
        ...

    def setup_controller(self, controller: Controller) -> None:
        ...

    def get_user_input(self) -> None:
        ...


class CLI:
    def display_message(self, message: str):
        print(message)

    def setup_controller(self, controller: Controller) -> None:
        self._controller = controller

    def get_user_input(self) -> None:
        error_msg = (
            f"Bitte geben Sie eine Zahl zwischen {self._controller._model._gues_range.min}"
            + f" und {self._controller._model._gues_range.max} an:"
        )
        self.display_message(error_msg)
        while True:
            try:
                self._user_eingabe = self.try_user_value()
                break
            except ValueError:
                self.display_message(error_msg)

    def try_user_value(self) -> int:
        user_eingabe = int(input())
        if user_eingabe not in list(
            range(
                self._controller._model._gues_range.min,
                self._controller._model._gues_range.max + 1,
            )
        ):
            raise ValueError
        return user_eingabe
