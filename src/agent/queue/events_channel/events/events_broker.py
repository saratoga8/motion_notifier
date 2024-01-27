from abc import ABC

from src.agent.queue.events_channel.broker import Broker
from src.agent.queue.events_channel.events.event import Event
from src.agent.queue.events_channel.events.events_subscriber import EventsSubscriber


class EventsBroker(Broker[Event], ABC):
    def __init__(self, subscribers: set[EventsSubscriber]):
        self._subscribers = subscribers

    @property
    def subscribers(self):
        return self._subscribers

    def add_item(self, item: Event):
        [subscriber.update(item) for subscriber in self._subscribers]
