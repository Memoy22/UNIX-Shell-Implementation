from abc import ABC, abstractmethod


class Command(ABC):
    """ Abstract class for all commands."""
    @abstractmethod
    def execute(self, args, stdin):
        pass
