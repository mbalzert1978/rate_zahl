from __future__ import annotations
from typing import TYPE_CHECKING, Protocol
import random

if TYPE_CHECKING:
    from ..helper.game_range import GameRange


class GameModel(Protocol):
    def is_game_over(self) -> bool:
        ...


class ModelRateZahl:
    def __init__(self, gues_range: GameRange, life: int = 3) -> None:
        self._gues_range = gues_range
        self._life = life
        self._to_gues = random.randint(*self._gues_range)

    def is_game_over(self) -> bool:
        return not self._life
