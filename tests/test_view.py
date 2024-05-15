import pytest

from src.rate_zahl.view.cli import CLI
from tests.stubs import ControllerStub


def test_init() -> None:
    view = CLI()
    stub = ControllerStub(view)

    assert view is not None
    assert view.mediator is stub


def test_view_no_mediator() -> None:
    view = CLI()

    with pytest.raises(AttributeError, match="The mediator is not set."):
        view.mediator


def test_show(capfd) -> None:
    view = CLI()

    view.show("Test Message.")
    out, _ = capfd.readouterr()

    assert out == "Test Message.\n"
