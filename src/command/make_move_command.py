from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from src.app import App
    from src.game.gamelogic import GameLogic
from src.command.command import Command


class MakeMove(Command):
    @property
    def app(self):
        return self.__app

    @app.setter
    def app(self, value: App):
        if not isinstance(value, App):
            raise ValueError(f"No valid App: {value}")
        self.__app = value

    @property
    def logic(self):
        return self.__logic

    @logic.setter
    def logic(self, value: GameLogic):
        if isinstance(value, GameLogic):
            self.__logic = value
        raise ValueError(f"No valid Gamelogic: {value}")
