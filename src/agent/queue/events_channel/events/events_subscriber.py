from src.agent.queue.events_channel.Subscriber import Subscriber
from src.agent.queue.events_channel.events.event import Event, State
import logging


class EventsSubscriber(Subscriber[Event]):
    def __init__(self, name):
        super().__init__(name)

    def update(self, event: Event):
        pass

    def give(self) -> Event | None:
        return None
