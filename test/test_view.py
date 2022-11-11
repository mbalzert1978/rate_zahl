import pytest
from ..src.view.cli import CLI
from unittest.mock import MagicMock
import builtins


class RepoStub:
    _gues_range = (1, 10)


class ControllerStub:
    _model = RepoStub()


@pytest.fixture
def cli() -> CLI:
    v = CLI()
    v.setup_controller(ControllerStub)
    return v


def test_display_message(cli, capsys):
    cli.display_message("test")
    captured = capsys.readouterr()
    assert captured.out == "test\n"


def test_get_user_input(cli, monkeypatch):
    monkeypatch.setattr(builtins, "input", lambda: "1")
    cli.get_user_input()
    assert cli._user_input == 1


def test_get_user_input_fail_out_of_range(cli, monkeypatch):
    monkeypatch.setattr(builtins, "input", lambda: "165")
    with pytest.raises(ValueError) as exc:
        cli.try_user_value()
    assert "Out of range error." in str(exc.value)


def test_get_user_input_fail_no_number(cli, monkeypatch):
    monkeypatch.setattr(builtins, "input", lambda: "A")
    with pytest.raises(ValueError) as exc:
        cli.try_user_value()
    assert "Bitte geben Sie eine Zahl zwischen %s und %s an"
