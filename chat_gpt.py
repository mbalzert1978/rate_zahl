import random
from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, *args, **kwargs) -> None:
        pass


class View(Observer):
    def update(self, message) -> None:
        print(message)


class Model(ABC):
    @abstractmethod
    def update(self, guess) -> None:
        pass


class NumberModel(Model):
    def __init__(self, game) -> None:
        self.game = game
        self.target = random.randint(1, 100)
        self.game.register(self)

    def update(self, guess) -> None:
        if guess == self.target:
            self.game.notify_observers("Sie haben gewonnen!")
        elif guess < self.target:
            self.game.notify_observers("Die gesuchte Zahl ist höher.")
            self.game.lives -= 1
        else:
            self.game.notify_observers("Die gesuchte Zahl ist niedriger.")
            self.game.lives -= 1


class Game:
    def __init__(self, model: Model) -> None:
        self.views = []
        self.lives = 7
        self.model = model

    def register(self, views) -> None:
        self.views.append(views)

    def update_views(self, message) -> None:
        for view in self.views:
            view.update(message)

    def play(self) -> None:
        while self.lives > 0:
            guess = int(input("Rate eine Zahl zwischen 1 und 100: "))
            self.update_views("Sie haben {} gewählt.".format(guess))
            self.model.update(guess)
        else:
            self.update_views(
                "Sie haben verloren. Das Ziel war {}.".format(
                    self.model.target
                )
            )


if __name__ == "__main__":
    model = NumberModel()
    game = Game(model)
    view = View()
    game.register(view)
    game.play()
