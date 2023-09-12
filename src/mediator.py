from __future__ import annotations

from abc import ABC


class Mediator(ABC):
    def notify(self, sender: BaseComponent, event: str) -> None:
        ...


class BaseComponent:
    def __init__(self, mediator: Mediator | None = None) -> None:
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        if not self._mediator:
            msg = "The mediator is not set."
            raise AttributeError(msg)
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator
