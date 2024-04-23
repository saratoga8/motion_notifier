import logging
import time

from src.agent.queue.events_channel.events.event import Event
from src.agent.queue.events_channel.events.events_broker import EventsBroker
from src.agent.queue.events_channel.events.events_subscriber import EventsSubscriber
from src.agent.queue.events_channel.events.notifications.notification_event import (
    NotificationEvent,
)

eventPath = "/from/path"


def test_dispatch_event_to_subscriber(caplog):
    caplog.set_level(logging.DEBUG)

    sender = EventsSubscriberSender()
    receiver = EventsSubscriberReceiver()

    broker = EventsBroker({sender, receiver})

    broker.start()
    broker.stop()

    assert receiver.is_updated(), "Receiver did not update"
    assert len(broker.events) == 0, "There is still existing event"


def test_event_not_dispatched(caplog):
    caplog.set_level(logging.DEBUG)

    sender = EventsSubscriberSender()
    decliner = EventsSubscriberDecliner()

    broker = EventsBroker({sender, decliner})

    broker.start()
    time.sleep(0.5)
    broker.stop()

    assert len(broker.events) == 1, "Invalid number of existing events"


def generateSenders():


def test_dispatch_all_events(caplog):
    caplog.set_level(logging.DEBUG)

    senders: EventsSubscriber[] = generateSenders()
    receivers: EventsSubscriber[] = generateReceivers()

    broker = EventsBroker(senders)
    broker.start()
    [broker.add_item(receiver) for receiver in receivers]

    time.sleep(0.5)
    broker.stop()

    assert len(broker.events) == 0, "There are still existing events"


class EventsSubscriberSender(EventsSubscriber):
    def __init__(self):
        EventsSubscriber.__init__(self, "Sender")
        event = NotificationEvent[str](eventPath)
        self._events.put(event)

    def update(self, event: Event):
        pass


class EventsSubscriberReceiver(EventsSubscriber):
    def __init__(self):
        EventsSubscriber.__init__(self, "Receiver")
        self.__updated = False

    def update(self, event: Event):
        super().update(event)
        self.__updated = event.data == eventPath

    def give(self) -> Event | None:
        pass

    def is_updated(self) -> bool:
        return self.__updated


class EventsSubscriberDecliner(EventsSubscriber):
    def __init__(self):
        EventsSubscriber.__init__(self, "Decliner")
        self.__updated = False

    def update(self, event: Event):
        pass

    def give(self) -> Event | None:
        pass

class EventsSubscriberSenderNumbered(EventsSubscriber):
    def __init__(self, number: int):
        EventsSubscriber.__init__(self, f"Sender{number}")
        event = NotificationEvent[int](number)
        self._events.put(event)

    def update(self, event: Event):
        pass

class EventsSubscriberReceiverNumberd(EventsSubscriber):
    def __init__(self, number: int):
        EventsSubscriber.__init__(self, f"Receiver{number}")
        self.__updated = False
        self.__number = number

    def update(self, event: Event):
        if event.data == self.__number:
            super().update(event)
            self.__updated = True

    def give(self) -> Event | None:
        pass

    def is_updated(self) -> bool:
        return self.__updated
