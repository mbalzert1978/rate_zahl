from src.rate_zahl.mediator import BaseComponent
from src.rate_zahl.model import ValueObject
from src.rate_zahl.player.human import Player
from src.rate_zahl.view import View


class ControllerStub:
    def __init__(self, component: BaseComponent) -> None:
        self.component = component
        self.component._mediator = self
        self.commands = {}

    def notify(self, sender: BaseComponent, event: str) -> None:
        self.commands[sender] = event


class ViewStub(View):
    def __init__(self) -> None:
        self.commands = []

    def show(self, msg: str) -> None:
        self.commands.append(msg)


class PlayerStub(Player):
    def __init__(self) -> None:
        self.commands = []

    def get_input(self) -> None:
        self.commands.append("get_input")


class ModelStub[T](ValueObject):
    def __init__(self, to_gues: int = 5) -> None:
        self.to_gues = to_gues
        self.commands = []

    @property
    def value(self) -> T:
        return self.to_gues

    def is_game_over(self) -> None:
        self.commands.append("is_game_over")
        self.mediator.notify(self, None)

    def is_guessed(self, gues: int) -> None:
        self.commands.append(gues)
