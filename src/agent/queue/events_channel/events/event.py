import time
from abc import ABC, abstractmethod
from enum import Enum
from typing import TypeVar, Generic

DataType = TypeVar("DataType")


class State(Enum):
    GENERATED = 0
    RECEIVED = 2
    SENT = 1


class Event(ABC, Generic[DataType]):
    def __init__(self):
        self.__id = int(round(time.time()))
        self.__from = None
        self.__state = State.GENERATED

    @property
    @abstractmethod
    def data(self) -> DataType:
        pass

    @property
    def state(self) -> State:
        return self.__state

    @state.setter
    def state(self, state: State):
        self.__state = state

    @state.getter
    def id(self) -> int:
        return self.__id
