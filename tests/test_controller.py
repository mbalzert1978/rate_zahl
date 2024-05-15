import pytest

from src.rate_zahl.controller import RateZahl
from tests.stubs import ModelStub, PlayerStub, ViewStub


@pytest.fixture()
def setup() -> tuple[ModelStub, ViewStub, PlayerStub, RateZahl]:
    model = ModelStub()
    view = ViewStub()
    player = PlayerStub()
    controller = RateZahl(view, model, player)
    return model, view, player, controller


def test_init(setup: tuple[ModelStub, ViewStub, PlayerStub, RateZahl]) -> None:
    model, view, player, controller = setup

    assert model.mediator is controller
    assert view.mediator is controller
    assert player.mediator is controller
    assert controller._model is model
    assert controller._view is view
    assert controller._player is player


def test_play(setup: tuple[ModelStub, ViewStub, PlayerStub, RateZahl]) -> None:
    model, view, player, controller = setup

    controller.play()
    assert view.commands == ["Guess a number between 1 and 100: "]
    assert model.commands == [0, "is_game_over"]
    assert player.commands == ["get_input"]


def test_show_sequence(
    setup: tuple[ModelStub, ViewStub, PlayerStub, RateZahl],
) -> None:
    _, view, _, controller = setup

    controller.show_sequence(("a", "b", "{value}"))
    assert view.commands == ["a", "b", "5"]


def test_notify_user_case_int(
    setup: tuple[ModelStub, ViewStub, PlayerStub, RateZahl],
) -> None:
    model, _, _, controller = setup

    controller.notify(model, "5")
    assert controller._guess == 5


def test_notify_user_case_big(
    setup: tuple[ModelStub, ViewStub, PlayerStub, RateZahl],
) -> None:
    model, view, _, controller = setup

    controller.notify(model, "big")
    assert view.commands == ["You guessed to big."]


def test_notify_user_case_small(
    setup: tuple[ModelStub, ViewStub, PlayerStub, RateZahl],
) -> None:
    model, view, _, controller = setup

    controller.notify(model, "small")
    assert view.commands == ["You guessed to small."]


def test_notify_user_case_guessed(
    setup: tuple[ModelStub, ViewStub, PlayerStub, RateZahl],
) -> None:
    model, view, _, controller = setup

    controller.notify(model, "guessed")
    assert view.commands == ["Won you guessed correctly.", "You win."]


def test_notify_user_case_gameover(
    setup: tuple[ModelStub, ViewStub, PlayerStub, RateZahl],
) -> None:
    model, view, _, controller = setup

    controller.notify(model, "gameover")
    assert view.commands == ["Game over.", "You lost.", "The number was 5"]


def test_notify_wrong_input(
    setup: tuple[ModelStub, ViewStub, PlayerStub, RateZahl],
) -> None:
    _, view, player, controller = setup

    controller.notify(player, "wrong")
    assert view.commands == ["Enter a number between 1 and 100!"]
    assert player.commands == ["get_input"]
