from abc import abstractmethod


class ScheduledTask:
    def __init__(self, line: str):
        if line:
            self.__exec_date = self._build_exec_date(line)
        else:
            raise ValueError('The sting for creating a scheduled task is empty')
        self._executed = False

    @property
    def execution_date(self) -> float:
        return self.__exec_date

    @abstractmethod
    def _build_exec_date(self, line) -> float:
        """
        Generate execution date from the given string
        :param line: text line when to run the task
        :return: timestamp of the execution date
        """
        pass

    @abstractmethod
    def exec(self) -> None:
        """
        Implementation of the task executing
        :return:
        """
        pass

    @property
    def is_executed(self):
        return self._executed

