from datetime import datetime

from croniter import croniter

from agent.scheduling.tasks.recurrent_scheduled_task import RecurrentScheduledTask


class CronScheduledTask(RecurrentScheduledTask):
    def __init__(self, line: str):
        self.__iter = croniter(line, datetime.today())
        super().__init__(line)

    def _build_exec_date(self, line) -> float:
        return self.__iter.get_next(datetime)

    def exec(self) -> None:
        super().exec()
