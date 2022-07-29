from abc import ABC, abstractmethod, abstractproperty


class Game(ABC):
    @abstractproperty
    def players(self):
        """list of players"""

    @abstractmethod
    def make_move_command(self):
        """make player move"""

    @abstractmethod
    def next_player(self):
        """make player move"""

    @abstractmethod
    def is_winner(self):
        """checks if there is a winner"""
