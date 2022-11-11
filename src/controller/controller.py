from __future__ import annotations
import tkinter as tk
from typing import TYPE_CHECKING, Protocol
from ..helper.text_messages import RateZahlMessages
from ..helper.canvas_configuration import CanvasConfiguration

if TYPE_CHECKING:
    from ..model.model import Repository
    from ..view.view import View


class Controller(Protocol):
    def __init__(self, model: Repository, view: View) -> None:
        ...

    def play(self) -> None:
        ...


class TKCZahlRaten(tk.Tk):
    def __init__(self, model, view) -> None:
        self._model = model
        self._view = view
        self._view.setup_controller(self)
        self.setup()

    def setup(self) -> None:
        cv = CanvasConfiguration
        self.title(RateZahlMessages.TITLE.value)
        self.config(bg=cv.GREY.value)
        self.geometry(cv.GEOMETRY.value)

    def play(self) -> None:
        pass


class ControllerZahlRaten:
    def __init__(self, model, view) -> None:
        self._model = model
        self._view = view
        self._view.setup_controller(self)

    def play(self) -> None:
        msg = RateZahlMessages
        view = self._view
        display = view.display_message
        game_over = self._model.is_game_over
        gues_n = str(self._model._to_gues)
        user_input = view.get_user_input
        display(msg.TITLE.value)
        while True:
            user_input()
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
        if self._view._user_input != self._model._to_gues:
            self.model = self._model.replace(self._model._lifes - 1)
            return False
        return True

    def give_hint(self) -> None:
        rzm = RateZahlMessages
        view = self._view.display_message
        if self._view._user_input > self._model._to_gues:
            view(rzm.TOBIG.value)
            return
        view(rzm.TOSMALL.value)
