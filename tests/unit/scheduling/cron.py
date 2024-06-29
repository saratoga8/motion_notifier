import time

from agent.scheduling.tasks.cron_task import CronScheduledTask


class DummyCronTask(CronScheduledTask):
    def __init__(self):
        super().__init__("* * * * *")


def test_task_run_in_minute():
    cur_date = time.time()
    task = CronScheduledTask("*/1 * * * *")
    assert (task.execution_date() - cur_date) == 0.0, "Invalid task's execution date"
