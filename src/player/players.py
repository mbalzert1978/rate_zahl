from abc import ABC
from dataclasses import dataclass


@dataclass
class Player(ABC):
    lifes: int


@dataclass
class HumanPlayer(Player):
    lifes: int


@dataclass
class CPUPlayer(Player):
    lifes: int
