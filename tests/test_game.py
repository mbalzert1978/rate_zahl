from unittest.mock import Mock

import pytest

from src.rate_zahl.core.app import Game
from src.rate_zahl.ports.data import DataPort
from src.rate_zahl.ports.interface import ViewPort
from src.rate_zahl.ports.player import PlayerPort
from src.rate_zahl.ports.score import ScorePort


@pytest.fixture()
def game() -> Game:
    view_port_mock = Mock(spec=ViewPort)
    score_port_mock = Mock(spec=ScorePort)
    data_port_mock = Mock(spec=DataPort)
    player_port_mock = Mock(spec=PlayerPort)
    return Game(view=view_port_mock, score=score_port_mock, persistence=data_port_mock, player=player_port_mock)


def test_game_is_won(game: Game) -> None:
    game._to_gues = 50  # Assuming direct assignment for testing
    assert game.is_game_won(50) is True, "The game should be won when the guess matches the target number."
