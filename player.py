from abc import ABC, abstractmethod
from random import randint

from view import View


class Player(ABC):
    """AbstractPlayerClass"""

    @abstractmethod
    def gues(self, error_fn: View.display_message):
        """gues the number"""


class HumanPlayer(Player):
    def gues(self, error_fn: View.display_message) -> int:
        valid = list(range(1, 11))
        while True:
            try:
                eingabe = int(input())
                if eingabe not in valid:
                    raise ValueError
                return eingabe
            except ValueError:
                error_fn("Bitte geben Sie eine Zahl ein.")

    def __str__(self) -> str:
        return "a Human Player"


class RandomCPU(Player):
    def gues(self, error_fn: View.display_message):
        return randint(1, 10)

    def __str__(self) -> str:
        return "a CPU Player"
