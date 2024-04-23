from copy import copy

from src.agent.queue.events_channel.subscriber import Subscriber
from src.agent.queue.events_channel.events.event import Event, State
from queue import SimpleQueue
import logging


class EventsSubscriber(Subscriber[Event]):
    def __init__(self, name):
        super().__init__(name)
        logging.debug(f"Building events subscriber {self.name}")
        self._events = SimpleQueue()

    def update(self, event: Event):
        event_copy = copy(event)
        self._events.put(event_copy)
        event.state = State.RECEIVED
        logging.debug(f"updated subscriber '{self.name}' by event: {event.id}")

    def give(self) -> Event | None:
        if not self._events.empty():
            event = self._events.get()
            event.state = State.GENERATED
            logging.debug(f"sending event {event.id} from subscriber '{self.name}'")
            return event
        return None
