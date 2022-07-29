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
