from abc import ABC, abstractproperty


class View(ABC):
    @abstractproperty
    def app(self):
        raise NotImplementedError()
