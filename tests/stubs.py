from src.mediator import BaseComponent


class ControllerStub:
    def __init__(self, component: BaseComponent) -> None:
        self.component = component
        self.component._mediator = self
        self.commands = {}

    def notify(self, sender: BaseComponent, event: str) -> None:
        self.commands[sender] = event
