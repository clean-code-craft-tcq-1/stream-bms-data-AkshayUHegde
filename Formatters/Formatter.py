from abc import ABC, abstractmethod


class Formatter(ABC):
    @abstractmethod
    def format(self, data):
        raise NotImplementedError
