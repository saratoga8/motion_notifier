import pytest

def test_receive_events():
    queue = async new EventsQueue().start()
    controller = async new Controller().start()
    queue.add_subscriber(controller)

