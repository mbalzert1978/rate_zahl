from __future__ import annotations
import random
from src.game.gamelogic import GameLogic
from src.view.view import View
from src.player.players import Player
from src.app import App


class RateZahl(App):
    def __init__(self, game, view, players) -> None:
        self.game: GameLogic = game
        self.view: View = view
        self.players: list[Player] = players
        self.active_player: Player = random.choice(self.players)

    @property
    def players(self) -> None:
        return self.__players

    @players.setter
    def players(self, value: list[Player]) -> None:
        if not isinstance(value, list):
            raise ValueError(f"No valid Playerlist: {value}")
        if not isinstance(next(iter(value)), Player):
            raise ValueError(f"No valid Playerlist: {value}")
        self.__players = value

    @property
    def view(self) -> None:
        return self.__view

    @view.setter
    def view(self, value: View) -> None:
        if not isinstance(value, View):
            raise ValueError(f"No valid Viewinstace: {value}")
        self.__view = value

    @property
    def game(self) -> None:
        return self.__game

    @game.setter
    def game(self, value: GameLogic) -> None:
        if not isinstance(value, GameLogic):
            raise ValueError(f"No valid Gameinstace: {value}")
        self.__game = value

    def set_active_player(self) -> None:
        activ_players_index = self.players.index(self.active_player)
        if not activ_players_index + 1 < len(self.players):
            self.active_player = self.players[0]
            return
        self.active_player = self.players[activ_players_index + 1]

    def create_ui(self) -> None:
        raise NotImplementedError

    def play(self) -> None:
        raise NotImplementedError
