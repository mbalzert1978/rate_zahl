import pytest

from src.controller import RateZahl
from tests.stubs import ModelStub, ViewStub


@pytest.fixture()
def setup():
    model = ModelStub()
    view = ViewStub()
    controller = RateZahl(view, model)
    return model, view, controller


def test_init(setup: tuple[ModelStub, ViewStub, RateZahl]) -> None:
    model, view, controller = setup

    assert model.mediator is controller
    assert view.mediator is controller
    assert controller._model is model
    assert controller._view is view


def test_play(setup: tuple[ModelStub, ViewStub, RateZahl]) -> None:
    model, view, controller = setup

    with pytest.raises(ValueError):
        controller.play()
    assert view.commands == {"get_user_input": True}
    assert model.commands == {"is_guessed": 0, "is_game_over": True}


def test_show_sequence(setup: tuple[ModelStub, ViewStub, RateZahl]) -> None:
    _, view, controller = setup

    controller.show_sequence(("a", "b", "{value}"))
    assert view.commands == {"a": "a", "b": "b", "5": "5"}


def test_notify_user_case_int(
    setup: tuple[ModelStub, ViewStub, RateZahl],
) -> None:
    model, _, controller = setup

    controller.notify(model, 5)
    assert controller._guess == 5


def test_notify_user_case_big(
    setup: tuple[ModelStub, ViewStub, RateZahl],
) -> None:
    model, view, controller = setup

    controller.notify(model, "big")
    assert view.commands == {"You guessed to big.": "You guessed to big."}


def test_notify_user_case_small(
    setup: tuple[ModelStub, ViewStub, RateZahl],
) -> None:
    model, view, controller = setup

    controller.notify(model, "small")
    assert view.commands == {"You guessed to small.": "You guessed to small."}


def test_notify_user_case_guessed(
    setup: tuple[ModelStub, ViewStub, RateZahl],
) -> None:
    model, view, controller = setup

    controller.notify(model, "guessed")
    assert view.commands == {
        "Won you guessed correctly.": "Won you guessed correctly.",
        "You win.": "You win.",
    }


def test_notify_user_case_gameover(
    setup: tuple[ModelStub, ViewStub, RateZahl],
) -> None:
    model, view, controller = setup

    controller.notify(model, "gameover")
    assert view.commands == {
        "Game over.": "Game over.",
        "You lost.": "You lost.",
        "The number was 5": "The number was 5",
    }
