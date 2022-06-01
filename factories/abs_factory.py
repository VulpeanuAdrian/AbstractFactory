import abc
from abc import abstractmethod

class AbsFactory(metaclass=abc.ABCMeta):
    @staticmethod
    @abstractmethod
    def create_economy():
        pass

    @staticmethod
    @abstractmethod
    def create_sport():
        pass

    @staticmethod
    @abstractmethod
    def create_luxury():
        pass
