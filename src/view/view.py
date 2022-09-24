from __future__ import annotations
from typing import TYPE_CHECKING, Protocol
from ..helper.text_messages import RateZahlMessages

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
        err_msg = RateZahlMessages.INPUTERR.value
        minimum, maximum = self.get_min_max()
        self.display_message(err_msg % (minimum, maximum))

        while True:
            try:
                self._user_eingabe = self.try_user_value()
                break
            except ValueError:
                self.display_message(err_msg % (minimum, maximum))

    def try_user_value(self) -> int:
        minimum, maximum = self.get_min_max()
        valid = list(range(minimum, maximum + 1))
        user_input = int(input())

        if user_input not in valid:
            raise ValueError
        return user_input

    def get_min_max(self):
        minimum = self._controller._model._gues_range.min
        maximum = self._controller._model._gues_range.max
        return minimum, maximum
