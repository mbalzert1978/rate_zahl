from view import ViewRateZahl
from model import ModelRateZahl


class ControllerZahlRaten:
    def __init__(self, model: ModelRateZahl, view: ViewRateZahl) -> None:
        self.model = model
        self.view = view

    def play(self):
        while True:
            self.view.print_Banner()
            self.nutzerzahl_abfragen()
            if self.model.prüfe_zahl():
                self.view.print_gewonnen(self.model.zu_raten)
                break
            if not self.model.ist_kleiner():
                self.view.print_tip(False)
            else:
                self.view.print_tip(True)
            if not self.model.ist_spiel_verloren():
                self.view.spiel_zu_ende_verlore(self.model.zu_raten)
                break

    def nutzerzahl_abfragen(self) -> None:
        valid = list(range(1, 11))
        while True:
            try:
                self.model.user_eingabe = int(input())
                if self.model.user_eingabe not in valid:
                    raise ValueError
                break
            except ValueError:
                self.view.print_rate_zahl_eingabe_fehler()
