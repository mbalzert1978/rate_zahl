from abc import ABC, abstractmethod
from random import randint


class Player(ABC):
    """AbstractPlayerClass"""

    @abstractmethod
    def gues(self, error_fn):
        """gues the number"""


class HumanPlayer(Player):
    def gues(self, error_fn) -> int:
        valid = list(range(1, 11))
        while True:
            try:
                eingabe = int(input())
                if eingabe not in valid:
                    raise ValueError
                return eingabe
            except ValueError:
                error_fn()


class RanadomCPU(Player):
    def gues(self, error_fn):
        return randint(0, 10)
