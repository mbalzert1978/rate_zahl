from __future__ import annotations

from src.controller import RateZahl
from src.model import Model
from src.player import AIPlayer, HumanPlayer
from src.view import CLI, NoOutput


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
