from __future__ import annotations
from typing import TYPE_CHECKING
from src.app import App

if TYPE_CHECKING:
    from src.player.players import Player
    from src.app import App
    from src.game.game import Game
    from src.view.view import View


class RateZahl(App):
    def __init__(self, game, view, players) -> None:
        self.game = game
        self.view = view
        self.players = players

    @property
    def players(self) -> None:
        return self.__players

    @players.setter
    def players(self, value: list[Player]) -> None:
        if not isinstance(value, list):
            raise ValueError(f"No valid Playerlist: {value}")
        if not isinstance(value, Game):
            raise ValueError(f"No valid Playerlist: {value}")
        self.__players = value

    @property
    def view(self) -> None:
        return self.__view

    @view.setter
    def view(self, value: View) -> None:
        if not isinstance(value, View):
            raise ValueError(f"No valid Viewinstace: {value}")
        self.__view = value

    @property
    def game(self) -> None:
        return self.__view

    @game.setter
    def game(self, value: Game) -> None:
        if not isinstance(value, Game):
            raise ValueError(f"No valid Gameinstace: {value}")
        self.__game = value

    def create_ui(self) -> None:
        raise NotImplementedError

    def play(self) -> None:
        raise NotImplementedError
