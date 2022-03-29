from player import HumanPlayer, RanadomCPU
from view import ViewRateZahl
from controller import ControllerZahlRaten
from model import ModelRateZahl


def main():
    game = setup_game()
    game.play()


def setup_game():
    m = ModelRateZahl()
    v = ViewRateZahl()
    list_of_players = [HumanPlayer(), RanadomCPU()]
    app = ControllerZahlRaten(model=m, view=v, players=list_of_players)
    return app


if __name__ == "__main__":
    main()
