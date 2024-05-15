import typing

T = typing.TypeVar("T")


class DataPort(typing.Protocol[T]):
    def get(self) -> T: ...
    def save(self, data: T) -> bool: ...
