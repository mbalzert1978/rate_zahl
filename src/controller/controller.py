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
        msg = RateZahlMessages
        view = self._view
        display = view.display_message
        game_over = self._model.is_game_over
        display(msg.TITLE.value)
        gues_n = str(self._model._to_gues)

        while True:
            view.get_user_input()
            if self.is_guessed():
                display(msg.WON.value % gues_n)
                break
            display(msg.LOSELIFE.value)
            self.give_hint()
            if game_over():
                display(msg.GAMEOVER.value % gues_n)
                break
            display(msg.FOOTER.value)

    def is_guessed(self) -> bool:
        if self._view._user_eingabe != self._model._to_gues:
            self._model._life -= 1
            return False
        return True

    def give_hint(self) -> None:
        rzm = RateZahlMessages
        view = self._view.display_message
        if self._view._user_eingabe > self._model._to_gues:
            view(rzm.TOBIG.value)
            return
        view(rzm.TOSMALL.value)
