from abc import ABC, abstractmethod
from typing import TypeVar, Generic

Item = TypeVar("Item")


class Subscriber(ABC, Generic[Item]):
    def __init__(self, name: str):
        self._name = name

    @abstractmethod
    def update(self, item: Item):
        pass

    @abstractmethod
    def give(self) -> Item:
        pass

    @property
    def name(self) -> str:
        return self._name
