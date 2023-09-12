from __future__ import annotations

import abc
import random
from typing import Any

from src.mediator import BaseComponent


class ValueObject(BaseComponent, abc.ABC):
    def is_guessed(self, gues: int) -> None:
        ...

    def is_game_over(self) -> None:
        ...

    @property
    def value(self) -> Any:
        ...


class Model(ValueObject):
    def __init__(self, to_gues: int | None = None, life: int = 3) -> None:
        self.to_gues = to_gues or random.randint(1, 100)
        self.life = life

    @property
    def value(self) -> Any:
        return self.to_gues

    def is_guessed(self, guess: int) -> None:
        if guess == self.to_gues:
            msg = "guessed"
        elif guess > self.to_gues:
            msg = "big"
        else:
            msg = "small"
        self.mediator.notify(self, msg)

    def is_game_over(self) -> None:
        self.life -= 1
        if self.life > 0:
            return
        self.mediator.notify(self, "gameover")
