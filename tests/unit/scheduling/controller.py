import logging
import time

from src.agent.scheduling.controller import Controller
from src.agent.scheduling.tasks.scheduled_task import ScheduledTask


class DummyOneTimeTask(ScheduledTask):
    def __init__(self, sleep_seconds: float):
        self.__sleep_sec = sleep_seconds
        super().__init__('bla')

    @property
    def sleep_sec(self):
        return self.__sleep_sec

    def _build_exec_date(self, line) -> float:
        return time.time() + self.sleep_sec

    def exec(self) -> None:
        logging.debug(f'Executing a task at the time: {self.execution_date}. Current time is {time.time()}')
        self._executed = True


class DummyController(Controller):
    def __init__(self, tasks: list[ScheduledTask]):
        super().__init__()
        self._tasks = tasks


def wait_until(predicate, timeout_sec: float, err_msg: str):
    step_sleep = .1
    steps_num = int(timeout_sec / step_sleep)
    for step in range(steps_num):
        if predicate():
            return
        else:
            time.sleep(step_sleep)
    assert predicate(), err_msg


def test_controller_single_task(caplog):
    caplog.set_level(logging.DEBUG)

    sleep_sec = 1.0
    tasks = [DummyOneTimeTask(sleep_sec)]
    for ind, task in enumerate(tasks):
        assert not task.is_executed, f"The task number {ind} should not be executed at start"

    controller = DummyController(tasks)

    controller.start()

    wait_until(lambda: len(controller.tasks) == 0, 3.0, "Not all the tasks in the controller removed")

    controller.stop()


def test_controller_multiple_tasks(caplog):
    caplog.set_level(logging.DEBUG)

    sleep_sec_1 = .5
    sleep_sec_2 = 1.0
    tasks = [DummyOneTimeTask(sleep_sec_1), DummyOneTimeTask(sleep_sec_2)]
    for ind, task in enumerate(tasks):
        assert not task.is_executed, f"The task number {ind} should not be executed at start"

    controller = DummyController(tasks)

    controller.start()

    wait_until(lambda: len(controller.tasks) == 1, 3.0, "The first task has not removed")
    wait_until(lambda: len(controller.tasks) == 0, 3.0, "Not all the tasks in the controller removed")

    controller.stop()
