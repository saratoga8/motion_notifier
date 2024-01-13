from abc import ABC, abstractmethod

from src.agent.queue.events_channel.events.Parser import Parser


class Event(ABC):
    @abstractmethod
    def parse(self, parser: Parser):
        pass
