from __future__ import annotations
from typing import TYPE_CHECKING, Protocol
from ..helper.text_messages import RateZahlMessages

if TYPE_CHECKING:
    from ..model.model import GameModel
    from ..view.view import View


class Controller(Protocol):
    def __init__(self, model: GameModel, view: View) -> None:
        ...

    def play(self) -> None:
        ...


class ControllerZahlRaten:
    def __init__(self, model, view) -> None:
        self._model = model
        self._view = view

    def play(self):
        self._view.display_title(RateZahlMessages.DISPLAY_TITLE.value)
        while True:
            self.get_user_input()
            if self.is_number_guessed():
                self._view.display_message(
                    RateZahlMessages.DISPLAY_GAMEOVER_WON.value
                )
                break
            self._view.display_message(RateZahlMessages.DISPLAY_LIFE_LOST.value)
            if not self.ist_kleiner():
                self.give_hint(False)
            else:
                self.give_hint(True)
            if self._model.is_game_over():
                self._view.display_message(
                    RateZahlMessages.DISPLAY_GAMEOVER.value
                    + self._model._to_gues
                )
                break
            self._view.display_message(RateZahlMessages.DISPLAY_FOOTER.value)

    def is_number_guessed(self) -> bool:
        if self._user_eingabe != self._model._to_gues:
            self._model._life -= 1
            return False
        return True

    def ist_kleiner(self) -> bool:
        if self._user_eingabe > self._model._to_gues:
            return False
        return True

    def give_hint(self, is_smaller: bool):
        if is_smaller:
            self._view.display_message(RateZahlMessages.HINT_SMALL.value)
            return
        self._view.display_message(RateZahlMessages.HINT_BIG.value)

    def get_user_input(self) -> None:
        error_msg = (
            f"Bitte geben Sie eine Zahl zwischen {self._model._gues_range.min}"
            + f" und {self._model._gues_range.max} an:"
        )
        self._view.display_message(error_msg)
        while True:
            try:
                self._user_eingabe = int(input())
                if self._user_eingabe not in list(
                    range(
                        self._model._gues_range.min,
                        self._model._gues_range.max + 1,
                    )
                ):
                    raise ValueError
                break
            except ValueError:
                self._view.display_message(error_msg)
