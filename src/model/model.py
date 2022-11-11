from __future__ import annotations
import random
from ..helper.func import validate_range


class RateZahlRepo:
    _frozen = False

    def __init__(self, gues_range: tuple[int, int], lifes: int = 3) -> None:
        self._gues_range = validate_range(gues_range)
        self._lifes = lifes
        self._to_gues = random.randint(*self._gues_range)
        self._frozen = True

    def __delattr__(self, *args, **kwargs) -> None:
        if self._frozen:
            raise AttributeError("This object is frozen!")
        object.__delattr__(self, *args, **kwargs)

    def __setattr__(self, *args, **kwargs) -> None:
        if self._frozen:
            raise AttributeError("This object is frozen!")
        object.__setattr__(self, *args, **kwargs)

    def replace(self, remaining_lifes: int) -> RateZahlRepo:
        return RateZahlRepo(
            gues_range=(self._to_gues, self._to_gues), lifes=remaining_lifes
        )

    def is_game_over(self) -> bool:
        return not self._lifes
