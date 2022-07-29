from abc import ABC, abstractmethod, abstractproperty


class Command(ABC):
    @abstractproperty
    def app(self):
        """the controlling app"""
        raise NotImplementedError

    @abstractproperty
    def logic(self):
        """the game logic"""
        raise NotImplementedError

    @abstractmethod
    def execute(self) -> None:
        """execute the command"""
        raise NotImplementedError
