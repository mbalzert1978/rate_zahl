from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from model import ModelRateZahl
    from view import ViewRateZahl


class ControllerZahlRaten:
    def __init__(self, model: ModelRateZahl, view: ViewRateZahl) -> None:
        self.model = model
        self.view = view
        self.view.set_controller(self)
        self.model.set_controller(self)

    def play(self):
        self.view.display_header()
        while True:
            self.view.get_user_input(list(range(*self.model.range_)))
            if self.is_number_to_gues():
                self.view.display_won(self.model.zu_raten)
                break
            if not self.ist_kleiner():
                self.view.display_message(
                    "Leider Falsch geraten! Du verlierst ein Leben"
                )
                self.view.display_hint(False)
            else:
                self.view.display_message(
                    "Leider Falsch geraten! Du verlierst ein Leben"
                )
                self.view.display_hint(True)
            if self.model.ist_spiel_verloren():
                self.view.display_lost(self.model.zu_raten)
                break
            self.view.display_footer()

    def is_number_to_gues(self) -> bool:
        if self.user_eingabe != self.model.zu_raten:
            self.model.leben -= 1
            return False
        return True

    def ist_kleiner(self) -> bool:
        if self.user_eingabe > self.model.zu_raten:
            return False
        return True
