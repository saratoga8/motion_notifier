from src.agent.queue.events_channel.events.event import Event, DataType

from typing import Generic


class NotificationEvent(Event, Generic[DataType]):
    def get_data(self) -> DataType:
        pass

    def __init__(self):
        super().__init__()
