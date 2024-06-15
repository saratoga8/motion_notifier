from agent.scheduling.tasks.onetime_scheduled_task import OneTimeScheduledTask
from agent.scheduling.tasks.recurrent_scheduled_task import RecurrentScheduledTask


class DummyOneTimeScheduledTask(OneTimeScheduledTask):
    def __init__(self):
        super().__init__("bla")

    def _build_exec_date(self, line) -> float:
        pass

    def exec(self) -> None:
        super().exec()


class DummyRecurrentScheduledTask(RecurrentScheduledTask):
    def __init__(self):
        super().__init__("bla")

    def exec(self) -> None:
        super().exec()

    def _build_exec_date(self, line) -> float:
        pass


def test_onetime_task(caplog):
    task = DummyOneTimeScheduledTask()

    assert task.is_executed is False, "Task should not be executed at first"

    task.exec()

    assert task.is_executed is True, "Task should be executed"


def test_recurrent_task(caplog):
    task = DummyRecurrentScheduledTask()

    assert task.is_executed is False, "Task should not be executed at first"

    task.exec()

    assert task.is_executed is False, "Task should not be executed"
