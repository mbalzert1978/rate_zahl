import pytest

from src.view.cli import CLI
from tests.stubs import ControllerStub


@pytest.fixture()
def setup() -> tuple[CLI, ControllerStub]:
    view = CLI()
    stub = ControllerStub(view)
    return view, stub


def test_init() -> None:
    view = CLI()

    assert view is not None


def test_view_no_mediator() -> None:
    view = CLI()

    with pytest.raises(AttributeError, match="The mediator is not set."):
        view.mediator


def test_show(capfd) -> None:
    view = CLI()

    view.show("Test Message.")

    out, _ = capfd.readouterr()
    assert out == "Test Message.\n"


def test_get_user_input(
    monkeypatch: pytest.MonkeyPatch,
    setup: tuple[CLI, ControllerStub],
) -> None:
    monkeypatch.setattr("builtins.input", lambda: 5)
    view, controller = setup

    view.get_user_input()
    assert controller.commands == {view: 5}


def test_get_user_input_negative(
    monkeypatch: pytest.MonkeyPatch,
    setup: tuple[CLI, ControllerStub],
    capfd,
) -> None:
    input_values = ["not_an_integer", "42"]

    def call():
        return input_values.pop(0)

    monkeypatch.setattr("builtins.input", call)
    view, controller = setup

    view.get_user_input()
    out, _ = capfd.readouterr()

    guess1, error, guess2, _ = out.split("\n")

    assert guess1 == guess2 == "Guess a number between 1 and 100: "
    assert error == "Enter a number between 1 and 100!"
    assert controller.commands == {view: 42}
