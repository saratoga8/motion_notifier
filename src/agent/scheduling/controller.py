import logging
import threading
import time

from src.agent.scheduling.config_manager import SchedulerConfigManager
from src.agent.scheduling.tasks.scheduled_task import ScheduledTask


class Controller:
    def __init__(self, config_path=""):
        self.__conf_mngr = SchedulerConfigManager(config_path)
        self._tasks: list[ScheduledTask] = self.__conf_mngr.build_tasks()
        self.__running: bool = False
        self.__lock = threading.Lock()

    def __is_running(self):
        with self.__lock:
            return self.__running

    def start(self):
        if not self.__is_running():
            self.__running = True
            threading.Thread(
                target=self.__observe_tasks,
                name="ScheduledTasksController",
                daemon=True,
            ).start()
        else:
            logging.warning("Can not start tasks observing. It's already running")

    def __observe_tasks(self):
        logging.debug("Starting tasks observing")
        while self.__is_running():
            self.__execute_tasks()
            self.__del_executed_tasks()
            time.sleep(0.1)

    def __execute_tasks(self):
        tasks_copy = self._tasks.copy()
        for task in tasks_copy:
            current_timestamp = time.time()
            if not task.is_executed and (task.execution_date <= current_timestamp):
                task.exec()
        self._tasks = tasks_copy

    def __del_executed_tasks(self):
        tasks_copy = self._tasks.copy()
        for task in self._tasks:
            if task.is_executed:
                logging.debug("Removing task")
                tasks_copy.remove(task)
        if len(tasks_copy) < len(self._tasks):
            self._tasks = tasks_copy

    def stop(self):
        logging.debug("stopping tasks observing")
        with self.__lock:
            self.__running = False

    @property
    def tasks(self):
        return self._tasks
