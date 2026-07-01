
from abc import ABC, abstractmethod

class Strategy(ABC):
    @property
    @abstractmethod

    def name(self) -> str:
        pass

    @abstractmethod
    def generate_signals (self, data):
        pass
