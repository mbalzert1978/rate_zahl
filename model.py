from abc import ABC, abstractmethod
from dataclasses import dataclass
import random


@dataclass
class Model(ABC):
    pass


@dataclass
class GameModel(Model):
    life: int = 3

    @abstractmethod
    def is_game_lost(self) -> bool:
        """returns if the game is lost or not"""


@dataclass
class GuessTheNumberGameModel(GameModel):
    to_guess: int = random.randint(1, 10)
    user_input: int = None

    def is_game_lost(self) -> bool:
        return not self.life

    def is_number_to_search(self) -> bool:
        if self.user_input != self.to_guess:
            self.life -= 1
            return False
        return True

    def is_lower(self) -> bool:
        if self.user_input > self.to_guess:
            return False
        return True
