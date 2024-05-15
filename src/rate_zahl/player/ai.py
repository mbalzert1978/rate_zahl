import random

from src.rate_zahl.player.human import Player

RANGE = 1, 100


class AIPlayer(Player):
    def __init__(self, test_value: int | None = None) -> None:
        self.test_value = test_value

    def __repr__(self) -> str:
        return f"{__class__.__name__}()"

    def get_input(self) -> None:
        self.mediator.notify(
            self,
            str(self.test_value or random.randint(*RANGE)),
        )
