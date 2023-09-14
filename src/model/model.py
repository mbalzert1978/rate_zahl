from __future__ import annotations

import abc
import random
from typing import Generic, TypeVar

from src.mediator import BaseComponent
from src.model.enums import GameState, Hint

T = TypeVar("T")


class ValueObject(BaseComponent, abc.ABC, Generic[T]):
    def is_guessed(self, gues: int) -> None:
        ...

    def is_game_over(self) -> None:
        ...

    @property
    def value(self) -> T:
        ...


class Model(ValueObject):
    def __init__(self, to_gues: int | None = None, life: int = 3) -> None:
        self.to_gues = to_gues or random.randint(1, 100)
        self.life = life
        super().__init__()

    @property
    def value(self) -> T:
        return self.to_gues

    def __repr__(self) -> str:
        return (
            f"{__class__.__name__}(to_gues={self.to_gues}, life={self.life})"
        )

    def is_guessed(self, guess: int) -> None:
        if guess == self.to_gues:
            msg = GameState.GUESSED
        elif guess > self.to_gues:
            msg = Hint.BIG
        else:
            msg = Hint.SMALL
        self.mediator.notify(self, msg)

    def is_game_over(self) -> None:
        self.life -= 1
        if self.life > 0:
            return
        self.mediator.notify(self, GameState.GAME_OVER)
