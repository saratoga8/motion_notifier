from abc import ABC

from agent.scheduling.tasks.scheduled_task import ScheduledTask


class CronScheduledTask(ScheduledTask, ABC):
    def __init__(self, line: str):
        super().__init__(line)

    def _build_exec_date(self, line) -> int:
        return 1

    def exec(self) -> None:
        pass

