from __future__ import annotations

from ..observer import Observer, Subject


class CLI(Observer):
    def update(self, subject: Subject) -> None:
        if subject

    def display_title(self) -> None:
        print("RateSpiel 1.0")
        print("Erate eine zufällige Zahl mit 3 Leben. Viel Spaß")
        print("#" * 20)

    def display_footer(self) -> None:
        print("#" * 20)

    def display_game_over(self) -> None:
        print("Game Over")
        print("Die gesuchte Zahl wahr: %s")

    def display_game_won(self) -> None:
        print("Game Over")
        print("Du hast gewonnen")
        print("Du hast die gesuchte Zahl %s gefunden.")

    def display_lose_life(self) -> None:
        print("Leider Falsch geraten! Du verlierst ein Leben")

    def display_give_hint_to_big(self) -> None:
        print("Deine gewählte Zahl ist zu groß")

    def display_give_hint_to_small(self) -> None:
        print("Deine gewählte Zahl ist zu klein")

    def display_input_error(self) -> None:
        print("Bitte geben Sie eine Zahl zwischen %s und %s an")
