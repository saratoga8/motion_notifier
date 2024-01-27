from abc import ABC, abstractmethod
from typing import Generic, TypeVar

DataType = TypeVar("DataType")


class Broker(ABC, Generic[DataType]):
    @abstractmethod
    def add_item(self, item: DataType) -> None:
        pass
