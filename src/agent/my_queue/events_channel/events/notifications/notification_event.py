import string

from src.agent.my_queue.events_channel.events.event import Event

from typing import Generic, TypeVar

DataType = TypeVar("DataType")


class NotificationEvent(Event, Generic[DataType]):
    _data: string

    def __init__(self, path: string):
        super().__init__()
        self._data = path

    @property
    def data(self) -> DataType:
        return self._data
