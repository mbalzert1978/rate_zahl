from __future__ import annotations
from typing import TYPE_CHECKING
from ..helper.text_messages import RateZahlMessages
import tkinter as tk

if TYPE_CHECKING:
    from ..controller.controller import Controller


class MainFrame(tk.Frame):
    def __init__(self, master: tk.Tk) -> None:
        self.main_window = master
        self.grid()
        self.create_layout()

    def create_layout(self) -> None:
        title = tk.Label(
            self, text="Please enter your information: ", bg="lightgrey"
        )

    def display_message(self, message: str) -> None:
        ...

    def setup_controller(self, controller: Controller) -> None:
        self._controller = controller

    def get_user_input(self) -> None:
        ...
