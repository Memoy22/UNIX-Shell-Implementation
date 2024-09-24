from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self, args: list[str], stdin: str | list[str]):
        pass
