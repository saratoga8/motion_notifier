import threading
import time
from abc import ABC

from src.agent.queue.events_channel.broker import Broker
from src.agent.queue.events_channel.events.event import Event, State
from src.agent.queue.events_channel.events.events_subscriber import EventsSubscriber
import logging


class EventsBroker(Broker[Event], ABC):
    __events: {Event} = set()
    __running: bool = False
    __lock = threading.Lock()

    def __init__(self, subscribers: set[EventsSubscriber]):
        self._subscribers = subscribers

    @property
    def subscribers(self):
        return self._subscribers

    def add_item(self, item: Event):
        [subscriber.update(item) for subscriber in self._subscribers]

    def _is_running(self):
        with self.__lock:
            return self.__running

    def _observe_events(self):
        logging.debug("Starting events observing")
        #        while self._is_running():
        self._check_for_events()
        self._dispatch_events()
        time.sleep(0.1)

    def start(self):
        __running = True
        threading.Thread(target=self._observe_events).start()

    def stop(self):
        with self.__lock:
            self.__running = False
        self._clean_events()

    def _clean_events(self):
        for event in self.__events:
            if event.state == State.RECEIVED:
                logging.debug(f"Removing event: {event.id}")
                self.__events.remove(event)

    def _dispatch_events(self):
        for event in self.__events:
            [subscriber.update(event) for subscriber in self._subscribers]

    def _check_for_events(self):
        for subscriber in self._subscribers:
            event = subscriber.give()
            if event is not None:
                event.state = State.SENT
                logging.debug(f"adding the event '{event.id}' to the queue")
                self.__events.add(event)
