import logging

from src.agent.scheduling.tasks.scheduled_task import ScheduledTask


class SchedulerConfigManager:
    def __init__(self, path=""):
        self.__path = path

    def build_tasks(self):
        tasks: [ScheduledTask] = []
        if self.__path:
            try:
                with open(self.__path) as file:
                    tasks = [self.__build_task(line) for line in file.readline()]
            except OSError as err:
                logging.error(f"Can not read from {self.__path}: {err}")
        return tasks

    def __build_task(self, line: str) -> ScheduledTask:
        return ScheduledTask(line)
