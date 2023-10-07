from __future__ import annotations
import abc


class Subject(abc.ABC):
    @abc.abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abc.abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abc.abstractmethod
    def notify(self) -> None:
        pass


class Observer(abc.ABC):
    @abc.abstractmethod
    def update(self, subject: Subject) -> None:

        pass
