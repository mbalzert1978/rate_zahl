from typing import Generator, Sequence


def range_inclusiv(start, stop) -> Generator[int, None, None]:
    return (x for x in range(start, stop + 1))


def validate_range(value: tuple[int, int]) -> tuple[int, int]:
    min, max = abs_sequence(value)
    min, max = set_min_lt_max(min, max)
    return (min, max)


def set_min_lt_max(min: int, max: int) -> tuple[int, int]:
    if min > max:
        min, max = max, min
    return min, max


def abs_sequence(value: Sequence[int]) -> tuple[int, ...]:
    return tuple(abs(x) for x in value)
