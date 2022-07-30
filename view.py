from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from controller import ControllerZahlRaten


class ViewRateZahl:
    def __init__(self) -> None:
        self.controller: ControllerZahlRaten = None

    def set_controller(self, value) -> None:
        self.controller = value

    def display_header(self) -> None:
        print("RateSpiel 1.0")
        print("Erate eine zufällige Zahl mit 3 Leben. Viel Spaß")
        print("#" * 20)

    def display_footer(self) -> None:
        print("#" * 20)

    def display_message(self, message):
        print(message)

    def display_won(self, zahl: int):
        print("Game Over")
        print("Richtig geraten!")
        print(f"Die gesuchte Zahl war: {zahl}")

    def display_hint(self, ist_kleiner: bool):
        if not ist_kleiner:
            print("Deine gewählte Zahl ist zu groß")
            return
        print("Deine gewählte Zahl ist zu klein")

    def display_lost(self, zahl: int):
        print("Game Over")
        print(f"Die gesuchte Zahl war: {zahl}")

    def get_user_input(self, valid) -> None:
        self.display_message(
            f"Bitte geben Sie eine Zahl zwischen {valid[0]} und {valid[-1]} an"
        )
        while True:
            try:
                self.controller.user_eingabe = int(input())
                if self.controller.user_eingabe not in valid:
                    raise ValueError
                break
            except ValueError:
                self.display_message(
                    f"Bitte geben Sie eine Zahl zwischen {valid[0]}"
                    + " und {valid[-1]} an"
                )
