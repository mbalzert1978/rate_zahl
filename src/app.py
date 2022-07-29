from abc import ABC, abstractmethod, abstractproperty


class App(ABC):
    """Abstract Game Application"""

    @abstractproperty
    def game(self) -> None:
        """the game"""

    @abstractmethod
    def create_ui(self) -> None:
        """create the UI if nessesary"""

    @abstractmethod
    def play(self) -> None:
        """Starts the game"""
