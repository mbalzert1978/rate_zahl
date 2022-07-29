from abc import ABC, abstractmethod
import random


class GameLogic(ABC):
    to_gues: int = random.randint(1, 10)

    @abstractmethod
    def gues(self):
        """make a gues"""

    @abstractmethod
    def is_winner(self):
        """checks if there is a winner"""
