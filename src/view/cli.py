from __future__ import annotations

import abc

from src.assets import GAMETEXT
from src.mediator import BaseComponent
from src.model.enums import GameState


class View(BaseComponent, abc.ABC):
    @abc.abstractmethod
    def show(self, msg: str) -> None:
        ...

    @abc.abstractmethod
    def get_user_input(self) -> None:
        ...


class CLI(View):
    def show(self, msg: str) -> None:
        print(msg)

    def get_user_input(self) -> None:
        while True:
            self.show(GAMETEXT.get(GameState.GUESSED))
            try:
                result = int(input())
            except ValueError:
                self.show(GAMETEXT.get(GameState.NUMBER))
                continue
            else:
                break
        self.mediator.notify(self, result)
