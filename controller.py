from abc import ABC
from dataclasses import dataclass
import random
from player import Player
from view import GuessTheNumberCLI, View
from model import GameModel


class Controller(ABC):
    pass


@dataclass
class GuessTheNumberController:
    model: GameModel

    def __init__(
        self, model: GameModel, players: list[Player], view: View
    ) -> None:
        self.model = model
        self.view = view
        self.players = players

    def play(self):
        random.shuffle(self.players)
        self.view.display_header()
        for player in self.players:
            if not self.model.life:
                self.model.life = 3
            while True:
                self.view.display_message(
                    f"{player} : Bitte geben Sie eine Zahl von 1-10 ein: "
                )
                self.model.user_input = player.gues(self.view.display_message)
                if self.model.is_number_to_search():
                    self.view.display_message(
                        (
                            "Game Over\n",
                            "Richtig geraten!\n",
                            f"Die gesuchte Zahl war: {self.model.to_guess}",
                        )
                    )
                    break
                self.view.display_message(
                    "Leider Falsch, deine Zahl war zu groß."
                ) if not self.model.is_lower() else self.view.display_message(
                    "Leider Falsch, deine Zahl war zu klein."
                )
                if self.model.is_game_lost():
                    self.view.display_message(
                        (
                            "Game Over\n",
                            "Leider verloren.\n",
                            f"Die gesuchte Zahl war: {self.model.to_guess}",
                        )
                    )
                    break
                self.view.display_footer()
