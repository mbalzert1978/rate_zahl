import pytest

from src.player.ai import AIPlayer
from src.player.human import HumanPlayer
from tests.stubs import ControllerStub


@pytest.fixture()
def setup() -> tuple[HumanPlayer, ControllerStub]:
    hp = HumanPlayer()
    stub = ControllerStub(hp)
    return hp, stub


def test_get_user_input(
    monkeypatch: pytest.MonkeyPatch,
    setup: tuple[HumanPlayer, ControllerStub],
) -> None:
    monkeypatch.setattr("builtins.input", lambda: "5")
    hp, controller = setup
    hp.get_input()

    assert controller.commands == {hp: "5"}


def test_get_ai_input():
    ai = AIPlayer(test_value=5)
    stub = ControllerStub(ai)

    ai.get_input()

    assert stub.commands == {ai: "5"}
