from src.mediator import BaseComponent
from src.model import ValueObject
from src.view import View


class ControllerStub:
    def __init__(self, component: BaseComponent) -> None:
        self.component = component
        self.component._mediator = self
        self.commands = {}

    def notify(self, sender: BaseComponent, event: str) -> None:
        self.commands[sender] = event


class ViewStub(View):
    def __init__(self) -> None:
        self.commands = {}

    def show(self, msg: str) -> None:
        self.commands[msg] = msg

    def get_user_input(self) -> None:
        self.commands["get_user_input"] = True


class ModelStu[T](ValueObject):
    def __init__(self, to_gues: int = 5) -> None:
        self.commands = {}
        self.to_gues = to_gues

    @property
    def value(self) -> T:
        return self.to_gues

    def is_game_over(self) -> None:
        self.commands["is_game_over"] = True
        self.mediator.notify(self, "")

    def is_guessed(self, gues: int) -> None:
        self.commands["is_guessed"] = gues
