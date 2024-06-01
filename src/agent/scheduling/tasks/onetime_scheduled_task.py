from abc import abstractmethod

from agent.scheduling.tasks.scheduled_task import ScheduledTask


class OneTimeScheduledTask(ScheduledTask):
    def __init__(self, line: str):
        super().__init__(line)

    @abstractmethod
    def exec(self) -> None:
        self._executed = True
        pass
