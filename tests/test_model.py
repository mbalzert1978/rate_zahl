import pytest

from src.rate_zahl.model.model import Model
from tests.stubs import ControllerStub


@pytest.fixture()
def setup() -> tuple[Model, ControllerStub]:
    model = Model(to_gues=3)
    stub = ControllerStub(model)
    return model, stub


def test_model_init() -> None:
    model = Model(to_gues=3)

    assert model is not None
    assert model.value == 3
    assert model.to_gues > 0
    assert model.to_gues < 100


def test_model_no_mediator() -> None:
    model = Model(to_gues=3)

    with pytest.raises(AttributeError, match="The mediator is not set."):
        model.mediator


def test_model_guessed(setup: tuple[Model, ControllerStub]) -> None:
    model, stub = setup

    model.is_guessed(3)

    assert stub.commands.get(model) == "guessed"


def test_model_to_big(setup: tuple[Model, ControllerStub]) -> None:
    model, stub = setup

    model.is_guessed(55)

    assert stub.commands.get(model) == "big"


def test_model_to_small(setup: tuple[Model, ControllerStub]) -> None:
    model, stub = setup

    model.is_guessed(2)

    assert stub.commands.get(model) == "small"


def test_game_is_over(setup: tuple[Model, ControllerStub]) -> None:
    model, stub = setup
    model.life = 1

    model.is_game_over()

    assert stub.commands.get(model) == "gameover"


def test_game_running(setup: tuple[Model, ControllerStub]) -> None:
    model, stub = setup

    model.is_game_over()

    assert stub.commands.get(model) is None
