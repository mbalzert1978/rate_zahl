from __future__ import annotations

from abc import ABC, abstractmethod


class Mediator(ABC):
    @abstractmethod
    def notify(self, sender: BaseComponent, event: str) -> None:
        ...


class BaseComponent:
    def __init__(self, mediator: Mediator | None = None) -> None:
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        if self._mediator is None:
            msg = "The mediator is not set."
            raise AttributeError(msg)
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator
