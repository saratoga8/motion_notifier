import threading

from time import sleep
from src.agent.queue.events_channel.events.event import Event, State
from src.agent.queue.events_channel.events.events_subscriber import EventsSubscriber
import logging


class EventsBroker:
    def __init__(self, subscribers: set[EventsSubscriber]):
        self.__subscribers = subscribers
        self.__events: {Event} = set()
        self.__running: bool = False
        self.__lock = threading.Lock()

    @property
    def events(self):
        return self.__events

    def add_subscriber(self, subscriber: EventsSubscriber):
        if subscriber:
            logging.debug(f"Adding subscriber {subscriber.name}")
            self.__subscribers.add(subscriber)
        else:
            logging.warn('Can not add an invalid subscriber')

    def __is_running(self):
        with self.__lock:
            return self.__running

    def __observe_events(self):
        logging.debug("Starting events observing")
        while self.__is_running():
            self.__check_for_events()
            self.__dispatch_events()
            self.__clean_events()
            sleep(0.1)

    def start(self):
        if not self.__is_running():
            self.__running = True
            threading.Thread(target=self.__observe_events).start()
        else:
            logging.warn('Can not start the broker. The broker is still running')

    def stop(self):
        logging.debug("stopping events observing")
        with self.__lock:
            self.__running = False

    def __clean_events(self):  # TODO: should be added clearing the old events: weakref
        events_copy = self.__events.copy()
        for event in self.__events:
            if event.state == State.RECEIVED:
                logging.debug(f"Removing event: {event.id}")
                events_copy.remove(event)
        if len(events_copy) != len(self.__events):
            self.__events = events_copy

    def __dispatch_events(self):
        for event in self.__events:
            [subscriber.update(event) for subscriber in self.__subscribers]

    def __check_for_events(self):
        for subscriber in self.__subscribers:
            event = subscriber.produce()
            if event is not None:
                event.state = State.SENT
                logging.debug(f"adding the event '{event.id}' to the queue")
                self.__events.add(event)
