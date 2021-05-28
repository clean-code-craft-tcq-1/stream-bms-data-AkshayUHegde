from abc import ABC, abstractmethod


class ParamGenerator(ABC):
    @abstractmethod
    def set_source(self, source):
        raise NotImplementedError

    @abstractmethod
    def get_param(self):
        raise NotImplementedError
