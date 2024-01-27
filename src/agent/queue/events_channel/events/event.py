import time
from abc import ABC, abstractmethod
from enum import Enum
from typing import TypeVar, Generic

DataType = TypeVar("DataType")


class State(Enum):
    GENERATED = 0
    PROCESSED = 1


class Event(ABC, Generic[DataType]):
    _id = int(round(time.time()))
    _from = None
    _state = State.GENERATED

    @abstractmethod
    def get_data(self) -> DataType:
        pass
