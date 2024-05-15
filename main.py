from __future__ import annotations

from src.rate_zahl.controller import RateZahl
from src.rate_zahl.model import Model
from src.rate_zahl.player import AIPlayer, HumanPlayer
from src.rate_zahl.view import CLI, NoOutput


def main() -> None:
    game = setup_human_player_game()
    game.play()


def setup_computer_player_game() -> RateZahl:
    m, v = Model(), NoOutput()
    p = AIPlayer()
    return RateZahl(v, m, p)


def setup_human_player_game() -> RateZahl:
    m, v = Model(), CLI()
    p = HumanPlayer()
    return RateZahl(v, m, p)


if __name__ == "__main__":
    main()
