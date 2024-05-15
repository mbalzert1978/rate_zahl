import typing

T_co = typing.TypeVar("T_co", covariant=True)


class ViewPort(typing.Protocol[T_co]):
    def show(self, message: str) -> None: ...
    def input(self) -> T_co: ...
