from __future__ import annotations

from typing import TYPE_CHECKING, Sequence

from src.assets import GAMETEXT
from src.mediator import BaseComponent, Mediator
from src.model.enums import GameState, Hint

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
        self._game_running = True

    def __repr__(self) -> str:
        return (
            f"RateZahl(guess={self._guess}, "
            f"game_running={self._game_running})"
        )

    def notify(self, _: BaseComponent, event: str) -> None:
        match event:
            case int(value):
                self._guess = value
            case Hint.BIG:
                self._view.show(GAMETEXT[Hint.BIG])
            case Hint.SMALL:
                self._view.show(GAMETEXT[Hint.SMALL])
            case GameState.GUESSED:
                self.show_sequence(GAMETEXT[GameState.WON])
                self._game_running = False
            case GameState.GAME_OVER:
                self.show_sequence(GAMETEXT[GameState.GAME_OVER])
                self._game_running = False
            case _:
                raise ValueError

    def show_sequence(self, msg: Sequence[str]) -> None:
        value = self._model.value
        for sentence in msg:
            self._view.show(sentence.format(value=value))

    def play(self) -> None:
        while self._game_running:
            self._view.get_user_input()
            self._model.is_guessed(self._guess)
            self._model.is_game_over()
