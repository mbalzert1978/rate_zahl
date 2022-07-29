from src.game.ratezahllogic import RateZahlLogic
from src.ratezahl import RateZahl
from src.view.view import View
from src.player.players import HumanPlayer, CPUPlayer


def setup_game():
    l = RateZahlLogic()
    v = View()
    p = [HumanPlayer(3), CPUPlayer(3)]
    app = RateZahl(l, v, p)
    return app


def app():
    pass


if __name__ == "__main__":
    app()
