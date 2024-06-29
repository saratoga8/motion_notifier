class CronScheduledTask(ABC):
    def __init__(self, line: str):
        super().__init__(line)

    def _build_exec_date(self, line) -> float:
        return 1.0

    def exec(self) -> None:
        pass
