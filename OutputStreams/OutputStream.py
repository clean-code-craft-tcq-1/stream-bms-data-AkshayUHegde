from abc import ABC, abstractmethod


class OutputStream(ABC):
    @abstractmethod
    def send(self, data):
        raise NotImplementedError
