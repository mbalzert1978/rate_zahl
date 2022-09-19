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
        self._view.setup_controller(self)

    def play(self):
        self._view.display_message(RateZahlMessages.DISPLAY_TITLE.value)
        while True:
            self._view.get_user_input()
            if self.is_number_guessed():
                self._view.display_message(
                    RateZahlMessages.DISPLAY_GAMEOVER_WON.value
                )
                break
            self._view.display_message(
                RateZahlMessages.DISPLAY_LIFE_LOST.value
            )
            if not self.is_user_input_smaller():
                self.give_hint(False)
            else:
                self.give_hint(True)
            if self._model.is_game_over():
                self._view.display_message(
                    RateZahlMessages.DISPLAY_GAMEOVER.value
                    + str(self._model._to_gues)
                )
                break
            self._view.display_message(RateZahlMessages.DISPLAY_FOOTER.value)

    def is_number_guessed(self) -> bool:
        if self._view._user_eingabe != self._model._to_gues:
            self._model._life -= 1
            return False
        return True

    def is_user_input_smaller(self) -> bool:
        if self._view._user_eingabe > self._model._to_gues:
            return False
        return True

    def give_hint(self, is_smaller: bool):
        if is_smaller:
            self._view.display_message(RateZahlMessages.HINT_SMALL.value)
            return
        self._view.display_message(RateZahlMessages.HINT_BIG.value)
