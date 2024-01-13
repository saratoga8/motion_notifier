from abc import ABC, abstractmethod


class Parser(ABC):
    @abstractmethod
    def parses(self, txt: str):
        pass
