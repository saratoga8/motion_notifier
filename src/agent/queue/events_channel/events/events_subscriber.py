from abc import ABC, abstractmethod

from src.agent.queue.events_channel.events.event import Event


class EventsSubscriber(ABC):
    @abstractmethod
    def update(self, even: Event) -> bool:
        pass

    @abstractmethod
    def receive(self, event: Event):
        pass
