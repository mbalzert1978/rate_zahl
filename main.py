from __future__ import annotations

from src.controller import RateZahl
from src.model import Model
from src.view import CLI


def main() -> None:
    game = setup_game()
    game.play()


def setup_game() -> RateZahl:
    m = Model()
    v = CLI()
    return RateZahl(v, m)


if __name__ == "__main__":
    main()
