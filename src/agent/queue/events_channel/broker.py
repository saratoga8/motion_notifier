from abc import ABC, abstractmethod
from typing import Generic, TypeVar

SubscriberType = TypeVar("SubscriberType")


class Broker(
    ABC, Generic[SubscriberType]
):  # TODO: Should be removed. Just use EventsBroker
    @abstractmethod
    def add_subscriber(self, subscriber: SubscriberType) -> None:
        pass
