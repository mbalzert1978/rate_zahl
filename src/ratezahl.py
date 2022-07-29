from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from src.player.players import Player
    from src.app import App
    from src.game.game import Game
from src.app import App


class RateZahl(App):
    @property
    def game(self) -> None:
        return self.__game

    @game.setter
    def game(self, value: Game) -> None:
        if not isinstance(value, Game):
            raise ValueError(f"No valid Gameinstace: {value}")
        self.__game = value

    def create_ui(self) -> None:
        raise NotImplementedError

    def play(self) -> None:
        raise NotImplementedError
