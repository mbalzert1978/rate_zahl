from src.game.gamelogic import GameLogic


class RateZahlLogic(GameLogic):
    def gues(self):
        raise NotImplementedError

    def is_winner(self):
        raise NotImplementedError
