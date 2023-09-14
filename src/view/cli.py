from __future__ import annotations

import abc

from src.mediator import BaseComponent


class View(BaseComponent, abc.ABC):
    @abc.abstractmethod
    def show(self, msg: str) -> None:
        ...


class CLI(View):
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    def show(self, msg: str) -> None:
        print(msg)


class NoOutput(View):
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    def show(self, _: str) -> None:
        pass
