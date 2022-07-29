from player import HumanPlayer, RandomCPU
from view import GuessTheNumberCLI
from controller import GuessTheNumberController
from model import GuessTheNumberGameModel


def main():
    game = setup_game()
    game.play()


def setup_game():
    m = GuessTheNumberGameModel()
    v = GuessTheNumberCLI()
    list_of_players = [HumanPlayer(), RandomCPU()]
    app = GuessTheNumberController(model=m, view=v, players=list_of_players)
    return app


if __name__ == "__main__":
    main()
