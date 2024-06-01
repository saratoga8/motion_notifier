import logging
import time

import pytest

from src.agent.my_queue.events_channel.events.events_broker import EventsBroker
from src.agent.scheduling.config_manager import SchedulerConfigManager


# @pytest.fixture(scope="session", autouse=True)
# def setup_session():
#     print("\nSetting up before all tests")
#     # Perform setup tasks here
#     yield
#     print("\nTearing down after all tests")
#     # Perform teardown tasks here
#
#
# # Fixture for setup tasks before each test
# @pytest.fixture(autouse=True)
# def setup_each_test():
#     print("\nSetting up before each test")
#     # Perform setup tasks here
#     yield
#     print("\nTearing down after each test")
#     # Perform teardown tasks here


def test_schedule_recurrent_task(caplog):
    caplog.set_level(logging.DEBUG)
    # SchedulerConfigManager('')
    # controller = Controller()
    #
    # broker = EventsBroker()
    # broker.start()
    # controller.subscribeTo(broker)
    #
    # controller.start()
    # assert len(broker.events) == 0, "The broker should not have any events"
    # time.sleep(1)
    # assert len(broker.events) == 1, "Invalid number of new events"
    # time.sleep(1)
    # assert len(broker.events) == 2, "Invalid number of new events"


