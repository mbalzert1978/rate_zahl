from view import ViewRateZahl
from model import ModelRateZahl


class ControllerZahlRaten:
    def __init__(self, model: ModelRateZahl, view: ViewRateZahl) -> None:
        self.model = model
        self.view = view

    def play(self):
        self.view.rate_zahl_header()
        while True:
            self.view.rate_zahl_eingabe_fehler()
            self.nutzerzahl_abfragen()
            if self.model.prüfe_zahl():
                self.view.rate_zahl_gewonnen(self.model.zu_raten)
                break
            if not self.model.ist_kleiner():
                self.view.rate_zahl_falsch_geraten()
                self.view.rate_zahl_tip(False)
            else:
                self.view.rate_zahl_falsch_geraten()
                self.view.rate_zahl_tip(True)
            if self.model.ist_spiel_verloren():
                self.view.rate_zahl_zu_ende_verlore(self.model.zu_raten)
                break
            self.view.rate_zahl_footer()

    def nutzerzahl_abfragen(self) -> None:
        valid = list(range(1, 11))
        while True:
            try:
                self.model.user_eingabe = int(input())
                if self.model.user_eingabe not in valid:
                    raise ValueError
                break
            except ValueError:
                self.view.rate_zahl_eingabe_fehler()
