from __future__ import annotations

from ..observer import Subject, Observer


class RateZahl(Subject):
    def __init__(self) -> None:
        self._observers: list[Observer] = []

    def play(self) -> None:
        while True:
            result = self.get_user_input()
            if self.is_guessed():
                display(msg.WON.value % gues_n)
                break
            display(msg.LOSELIFE.value)
            self.give_hint()
            if game_over():
                display(msg.GAMEOVER.value % gues_n)
                break
            display(msg.FOOTER.value)

    def get_user_input(self) -> int:
        while True:
            try:
                return int(input())
            except ValueError:
                continue

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)

    def is_guessed(self) -> bool:
        if self._view._user_input != self._model._to_gues:
            self._model._life -= 1
            return False
        return True

    def give_hint(self) -> None:
        rzm = RateZahlMessages
        view = self._view.display_message
        if self._view._user_input > self._model._to_gues:
            view(rzm.TOBIG.value)
            return
        view(rzm.TOSMALL.value)
