from typing import Protocol


class Repository(Protocol):
    def is_game_over(self) -> bool:
        ...
