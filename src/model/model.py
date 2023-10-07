from __future__ import annotations

import dataclasses
import random

from ..observer import Subject, Observer


@dataclasses.dataclass
class Model(Subject):
    to_gues: int = random.randint(1, 100)
    life: int = 3
    _observers: list[Observer] = dataclasses.field(default_factory=list)

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)
