from __future__ import annotations

from typing import TYPE_CHECKING, Sequence

from src.assets import GAMETEXT
from src.mediator import BaseComponent, Mediator
from src.model.enums import GameState, Hint

if TYPE_CHECKING:
    from src.model import ValueObject
    from src.player.human import Player
    from src.view import View


class RateZahl(Mediator):
    def __init__(self, view: View, model: ValueObject, player: Player) -> None:
        self._view = view
        self._view.mediator = self
        self._model = model
        self._model.mediator = self
        self._player = player
        self._player.mediator = self
        self._guess = 0
        self._game_running = True

    def __repr__(self) -> str:
        return (
            f"RateZahl(guess={self._guess}, game_running={self._game_running})"
        )

    def notify(self, _: BaseComponent, event: str) -> None:
        match event:
            case Hint.BIG:
                self._view.show(GAMETEXT.get(Hint.BIG))
            case Hint.SMALL:
                self._view.show(GAMETEXT.get(Hint.SMALL))
            case GameState.GUESSED:
                self.show_sequence(GAMETEXT.get(GameState.WON))
                self._game_running = False
            case GameState.GAME_OVER:
                self.show_sequence(GAMETEXT.get(GameState.GAME_OVER))
                self._game_running = False
            case str(value) if value.isdigit():
                self._guess = int(value)
            case None:
                self._game_running = False
            case _:
                self._view.show(GAMETEXT.get(GameState.NUMBER))
                self._player.get_input()

    def show_sequence(self, msg: Sequence[str]) -> None:
        value = self._model.value
        for sentence in msg:
            self._view.show(sentence.format(value=value))

    def play(self) -> None:
        while self._game_running:
            self._view.show(GAMETEXT.get(GameState.GUESSED))
            self._player.get_input()
            self._model.is_guessed(self._guess)
            self._model.is_game_over()
