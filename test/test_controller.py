from collections import namedtuple
from dataclasses import dataclass
from unittest.mock import MagicMock
from ..src.controller.controller import ControllerZahlRaten
import pytest


@pytest.fixture
def model():
    @dataclass
    class Model:
        _gues_range: tuple[int, int]
        _life: int
        _to_gues: int

    return Model((1, 10), 3, 5)


@pytest.fixture()
def view():
    view = MagicMock()
    view.display_message = MagicMock()
    view.setup_controller = MagicMock()
    view.get_user_input = MagicMock(return_value=3)
    yield view
    del view


@pytest.fixture
def setup(model, view):
    return ControllerZahlRaten(model, view)


def test_init(model, view: MagicMock):
    app = ControllerZahlRaten(model, view)
    assert app._model == model
    assert app._view == view
    assert view.setup_controller.called


def test_is_guesed(setup: ControllerZahlRaten):
    setup._view._user_eingabe = 5
    assert setup.is_guessed()


def test_is_guesed_fail(setup: ControllerZahlRaten):
    assert not setup.is_guessed()


def test_give_hint_small(setup: ControllerZahlRaten):
    setup._view._user_eingabe = 3
    setup.give_hint()
    assert setup._view.display_message.call_args.args == (
        "Deine gewählte Zahl ist zu klein",
    )


def test_give_hint_big(setup: ControllerZahlRaten):
    setup._view._user_eingabe = 6
    setup.give_hint()
    assert setup._view.display_message.call_args.args == (
        "Deine gewählte Zahl ist zu groß",
    )
