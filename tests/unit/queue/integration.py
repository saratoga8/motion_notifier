import logging
import time

from src.agent.queue.events_channel.events.event import Event, State
from src.agent.queue.events_channel.events.events_broker import EventsBroker
from src.agent.queue.events_channel.events.events_subscriber import EventsSubscriber
from src.agent.queue.events_channel.events.notifications.notification_event import (
    NotificationEvent,
)

eventPath = "/from/path"


class EventsSubscriberSender(EventsSubscriber):
    def __init__(self):
        super().__init__("Sender")

    def give(self) -> Event:
        event = NotificationEvent[str](eventPath)
        event.state = State.SENT
        logging.debug(f"sending event {event.id} from subscriber '{self.name}'")
        return event


class EventsSubscriberReceiver(EventsSubscriber):
    def __init__(self):
        super().__init__("Receiver")
        self.__updated: bool = False

    def update(self, event: Event):
        logging.debug(f"updated subscriber '{self.name}' by event: {event.id}")
        self.__updated = event.data == eventPath

    def is_updated(self) -> bool:
        return self.__updated


def is_event_in_state(event: Event, state: State) -> bool:
    return event.state == state


def test_dispatch_event_to_subscriber(caplog):
    caplog.set_level(logging.DEBUG)

    sender = EventsSubscriberSender()
    receiver = EventsSubscriberReceiver()

    broker = EventsBroker({sender, receiver})

    broker.start()

    time.sleep(2)
    assert receiver.is_updated(), "Receiver did not update"
    broker.stop()
