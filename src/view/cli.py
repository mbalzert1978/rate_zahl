from __future__ import annotations
from typing import TYPE_CHECKING
from ..helper.text_messages import RateZahlMessages
from ..helper.func import range_inclusiv

if TYPE_CHECKING:
    from ..controller.controller import Controller


class CLI:
    def display_message(self, message: str) -> None:
        print(message)

    def setup_controller(self, controller: Controller) -> None:
        self._controller = controller

    def get_user_input(self) -> None:
        err_msg = RateZahlMessages.INPUTERR.value
        self.display_message(err_msg % self._get_min_max())
        while True:
            try:
                self._user_input = self.try_user_value()
                break
            except ValueError:
                self.display_message(err_msg % self._get_min_max())

    def try_user_value(self) -> int:
        valid = list(range_inclusiv(*self._get_min_max()))
        user_input = int(input())
        if user_input not in valid:
            raise ValueError("Out of range error.")
        return user_input

    def _get_min_max(self) -> tuple[int, int]:
        return self._controller._model._gues_range
