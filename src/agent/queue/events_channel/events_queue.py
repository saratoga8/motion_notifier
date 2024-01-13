from src.agent.queue.events_channel.events_subscriber import EventsSubscriber


class EventsQueue:
    def __init__(self):
        self._subscribers = set()

    @property
    def subscribers(self):
        return self._subscribers
