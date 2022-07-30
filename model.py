from __future__ import annotations
from typing import TYPE_CHECKING
from dataclasses import dataclass, field
import random

if TYPE_CHECKING:
    from controller import ControllerZahlRaten


@dataclass
class ModelRateZahl:
    range_: tuple[int, int]
    leben: int = field(default=3, init=False)
    zu_raten: int = field(default=0, init=False)
    controller: ControllerZahlRaten = field(default=None, init=False)

    def __post_init__(self) -> None:
        self.zu_raten = random.randint(*self.range_)

    def ist_spiel_verloren(self) -> bool:
        return not self.leben

    def set_controller(self, value) -> None:
        self.controller = value
