import dataclasses
import random

from src.rate_zahl import strings
from src.rate_zahl.ports.data import DataPort
from src.rate_zahl.ports.interface import ViewPort
from src.rate_zahl.ports.player import PlayerPort
from src.rate_zahl.ports.score import ScorePort

MIN, MAX = 1, 100


def generate_seed() -> float:
    seed = random.gauss()
    random.seed(seed)
    return seed


@dataclasses.dataclass(kw_only=True)
class Game:
    seed: float = dataclasses.field(default_factory=generate_seed)
    view: ViewPort[int]
    score: ScorePort
    persistence: DataPort[str]
    player: PlayerPort
    _running: bool = dataclasses.field(default=True, init=False)
    _to_gues: int = dataclasses.field(init=False, default_factory=lambda: random.randint(MIN, MAX))  # noqa: S311

    def is_game_won(self, guess: int) -> bool:
        return guess == self._to_gues

    def end_game(self) -> None:
        self._running = False

    def play(self) -> None:
        while self._running:
            self.view.show(strings.en.HEADER)
            guess = self.view.input()
            if self.is_game_won(guess):
                self.view.show(strings.en.GUESSED_CORRECT.format(guess))
                self.view.show(strings.en.WIN.format(self.player.lives))
                self.view.show(strings.en.SEED.format(self.seed))
                self.end_game()
            else:
                self.player.loose_a_life()
                if self.player.is_alive():
                    self.view.show(strings.en.LIVES.format(self.player.lives))
                    self.view.show(strings.en.TRY_AGAIN)
                else:
                    self.view.show(strings.en.LOST)
                    self.view.show(strings.en.NUMBER_WAS.format(self._to_gues))
                    self.view.show(strings.en.SEED.format(self.seed))
                    self.end_game()
            self.score.next_round()
        self.persistence.save(self.score.serialize())

    def scores(self) -> str:
        return self.persistence.get()
