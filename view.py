from abc import ABC, abstractmethod
from dataclasses import dataclass
import tkinter as tk


@dataclass
class View(ABC):
    @abstractmethod
    def display_header(self) -> None:
        """Displays the Header"""

    @abstractmethod
    def display_footer(self) -> None:
        """Displays the footer"""

    @abstractmethod
    def display_message(self, message: str | tuple) -> None:
        """Displays an message"""


@dataclass
class GuessTheNumberCLI(View):
    def display_header(self) -> None:
        print("RateSpiel 1.0")
        print("Erate eine zufällige Zahl mit 3 Leben. Viel Spaß")
        print("#" * 20)

    def display_footer(self) -> None:
        print("#" * 20)

    def display_message(self, message: str | tuple) -> None:
        if isinstance(message, tuple):
            print(" ".join(message))
            return
        print(message)


@dataclass
class GuessTheNumberTki(View):
    def display_header(self) -> None:
        """Displays the Header"""
        pass

    def display_footer(self) -> None:
        """Displays the footer"""
        pass

    def display_message(message: str | tuple) -> None:
        """Displays an message"""
        pass
