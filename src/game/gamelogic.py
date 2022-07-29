from abc import ABC, abstractmethod
import random


class GameLogic(ABC):
    @abstractmethod
    def gues(self):
        """make a gues"""

    @abstractmethod
    def is_winner(self):
        """checks if there is a winner"""
