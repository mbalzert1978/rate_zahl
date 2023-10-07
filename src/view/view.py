from __future__ import annotations
from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from ..controller.controller import Controller


class View(Protocol):
    def display_message(self, message: str) -> None:
        ...

    def setup_controller(self, controller: Controller) -> None:
        ...

    def get_user_input(self) -> None:
        ...
