from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from src.mediator import BaseComponent, Mediator

if TYPE_CHECKING:
    from src.model import ValueObject
    from src.view import View


class RateZahl(Mediator):
    def __init__(self, view: View, model: ValueObject) -> None:
        self._view = view
        self._view.mediator = self
        self._model = model
        self._model.mediator = self
        self._guess = 0

    def notify(self, _: BaseComponent, event: str) -> None:
        match event:
            case int(value):
                self._guess = value
            case "guessed":
                self._view.show("Won you guessed correctly.")
                self._view.show("You win.")
                sys.exit()
            case "big":
                self._view.show("You guessed to big.")
            case "small":
                self._view.show("You guessed to small.")
            case "gameover":
                self._view.show("Game over.")
                self._view.show(f"The number was: {self._model.value}")
                sys.exit()
            case _:
                return

    def play(self) -> None:
        while True:
            self._view.get_user_input()
            self._model.is_guessed(self._guess)
            self._model.is_game_over()
