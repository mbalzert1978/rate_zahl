import random
from player import Player
from view import ViewRateZahl
from model import ModelRateZahl


class ControllerZahlRaten:
    def __init__(self, model: ModelRateZahl, players: list[Player], view: ViewRateZahl = None) -> None:
        self.model = model
        self.view = view
        self.players = players

    def play(self):
        random.shuffle(self.players)
        self.view.rate_zahl_header()
        for player in self.players:
            while True:
                self.view.rate_zahl_eingabe_fehler()
                self.model.user_eingabe = player.gues(self.view.rate_zahl_eingabe_fehler)
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
