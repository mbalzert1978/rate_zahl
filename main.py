from view import ViewRateZahl
from controller import ControllerZahlRaten
from model import ModelRateZahl


def main():
    game = setup_game()
    game.play()


def setup_game():
    m = ModelRateZahl((1, 100))
    v = ViewRateZahl()
    app = ControllerZahlRaten(model=m, view=v)
    return app


if __name__ == "__main__":
    main()
