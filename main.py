from src.view.cli import CLI
from src.controller.controller import ControllerZahlRaten
from src.model.model import RateZahlRepo


def main() -> None:
    game = setup_game()
    game.play()


def setup_game() -> ControllerZahlRaten:
    m = RateZahlRepo((1, 100))
    v = CLI()
    app = ControllerZahlRaten(model=m, view=v)
    return app


if __name__ == "__main__":
    main()
