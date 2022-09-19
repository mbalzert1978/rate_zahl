from src.view.view import CLI
from src.controller.controller import ControllerZahlRaten
from src.model.model import ModelRateZahl
from src.helper.game_range import GameRange


def main():
    game = setup_game()
    game.play()


def setup_game():
    gr = GameRange(1, 100)
    m = ModelRateZahl(gues_range=gr)
    v = CLI()
    app = ControllerZahlRaten(model=m, view=v)
    return app


if __name__ == "__main__":
    main()
