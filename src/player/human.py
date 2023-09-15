import abc

from src.mediator import BaseComponent


class Player(abc.ABC, BaseComponent):
    @abc.abstractmethod
    def get_input(self):
        raise NotImplementedError


class HumanPlayer(Player):
    def __repr__(self) -> str:
        return f"{__class__.__name__}()"

    def get_input(self) -> None:
        self.mediator.notify(self, input())
