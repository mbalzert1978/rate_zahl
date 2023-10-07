from ..src.model.model import ModelRateZahl
from ..src.helper.game_range import GameRange
import pytest


@pytest.fixture
def game_range():
    return GameRange(1, 10)


@pytest.fixture
def model(game_range):
    return ModelRateZahl(game_range)


def test_init(model):
    assert model._gues_range.min == 1
    assert model._gues_range.max == 10
    assert model._life == 3
    assert isinstance(model._to_gues, int)


def test_game_over(model):
    model._life = 0
    assert model.is_game_over()


def test_game_not_over(model):
    assert not model.is_game_over()
