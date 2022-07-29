from __future__ import annotations
from typing import TYPE_CHECKING
from src.app import App
from src.view.view import View

if TYPE_CHECKING:
    from src.app import App


class CLI(View):
    @property
    def app(self):
        return self.__app

    @app.setter
    def app(self, value):
        if not isinstance(value, App):
            raise ValueError(f"No valid Viewinstace: {value}")
        self.__app = value

    def display_header(self) -> None:
        raise NotImplementedError()

    def display_hint(self) -> None:
        raise NotImplementedError()

    def display_gamestate(self) -> None:
        raise NotImplementedError()

    def display_gues(self) -> None:
        raise NotImplementedError()

    def display_footer(self) -> None:
        raise NotImplementedError()
