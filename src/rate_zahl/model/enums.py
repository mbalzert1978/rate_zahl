from enum import StrEnum


class Hint(StrEnum):
    BIG = "big"
    SMALL = "small"


class GameState(StrEnum):
    NUMBER = "number"
    GUESSED = "guessed"
    WON = "won"
    GAME_OVER = "gameover"
