import pytest
from ..src.model.model import RateZahlRepo


def test_init() -> None:
    repo = RateZahlRepo(gues_range=(1, 1))
    assert repo._gues_range[0] == 1
    assert repo._gues_range[1] == 1
    assert repo._to_gues == 1
    assert repo._lifes == 3


def test_init_negative() -> None:
    repo = RateZahlRepo(gues_range=(-1, -2))
    assert repo._gues_range[0] == 1
    assert repo._gues_range[1] == 2


def test_init_max_lt_min() -> None:
    repo = RateZahlRepo(gues_range=(2, 1))
    assert repo._gues_range[0] == 1
    assert repo._gues_range[1] == 2


def test_imutable() -> None:
    repo = RateZahlRepo(gues_range=(1, 1))
    with pytest.raises(AttributeError) as exc:
        repo._gues_range = (1, 100)
    assert "This object is frozen!" in str(exc.value)


def test_game_over() -> None:
    repo = RateZahlRepo(gues_range=(1, 1), lifes=0)
    assert repo.is_game_over()


def test_game_not_over() -> None:
    repo = RateZahlRepo(gues_range=(1, 1), lifes=1)
    assert not repo.is_game_over()
