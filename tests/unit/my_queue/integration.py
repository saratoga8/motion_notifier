import logging
import time

from src.agent.my_queue.events_channel.events.event import Event
from src.agent.my_queue.events_channel.events.events_broker import EventsBroker
from src.agent.my_queue.events_channel.events.events_subscriber import EventsSubscriber
from src.agent.my_queue.events_channel.events.notifications.notification_event import (
    NotificationEvent,
)

from typing import TypeVar, Set, Type

SubscriberType = TypeVar("SubscriberType")


eventPath = "/from/path"


def test_dispatch_event_to_subscriber(caplog):
    caplog.set_level(logging.DEBUG)

    sender = EventsSubscriberSender()
    receiver = EventsSubscriberReceiver()

    broker = EventsBroker({sender, receiver})

    broker.start()
    time.sleep(0.2)
    broker.stop()

    assert receiver.is_updated(), "Receiver did not update"
    assert len(broker.events) == 0, "There is still existing event"


def test_event_not_dispatched(caplog):
    caplog.set_level(logging.DEBUG)

    sender = EventsSubscriberSender()
    decliner = EventsSubscriberDecliner()

    broker = EventsBroker({sender, decliner})

    broker.start()
    time.sleep(0.3)
    broker.stop()

    assert len(broker.events) == 1, "Invalid number of existing events"


def test_dispatch_all_events():
    subscribers_num = 1000
    senders = generate_senders(EventsSubscriberSenderNumbered, subscribers_num)
    receivers = generate_senders(EventsSubscriberReceiverNumbered, subscribers_num)

    broker = EventsBroker(senders | receivers)
    broker.start()
    time.sleep(0.3)
    broker.stop()

    assert len(broker.events) == 0, "There are still existing events"


def test_adding_subscriber(caplog):
    caplog.set_level(logging.DEBUG)

    sender = EventsSubscriberSender()
    decliner = EventsSubscriberDecliner()
    receiver = EventsSubscriberReceiver()

    broker = EventsBroker({sender, decliner})

    broker.start()
    time.sleep(0.3)
    assert len(broker.events) == 1, "Invalid number of existing events"
    broker.add_subscriber(receiver)
    time.sleep(0.3)

    broker.stop()
    assert receiver.is_updated(), "Receiver did not update"
    assert len(broker.events) == 0, "There is still existing event"


def generate_senders(class_type: Type[SubscriberType], num: int) -> Set[SubscriberType]:
    senders: Set[SubscriberType] = set()
    for i in range(num):
        if class_type == EventsSubscriberReceiverNumbered:
            senders.add(EventsSubscriberReceiverNumbered(i))
        if class_type == EventsSubscriberSenderNumbered:
            senders.add(EventsSubscriberSenderNumbered(i))
    return senders


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

    def produce(self) -> Event | None:
        pass

    def is_updated(self) -> bool:
        return self.__updated


class EventsSubscriberDecliner(EventsSubscriber):
    def __init__(self):
        EventsSubscriber.__init__(self, "Decliner")
        self.__updated = False

    def update(self, event: Event):
        pass

    def produce(self) -> Event | None:
        pass


class EventsSubscriberSenderNumbered(EventsSubscriber):
    def __init__(self, number: int):
        EventsSubscriber.__init__(self, f"Sender{number}")
        event = NotificationEvent[int](number)
        self._events.put(event)

    def update(self, event: Event):
        pass


class EventsSubscriberReceiverNumbered(EventsSubscriber):
    def __init__(self, number: int):
        EventsSubscriber.__init__(self, f"Receiver{number}")
        self.__updated = False
        self.__number = number

    def update(self, event: Event):
        if event.data == self.__number:
            super().update(event)
            self.__updated = True

    def produce(self) -> Event | None:
        pass

    def is_updated(self) -> bool:
        return self.__updated
