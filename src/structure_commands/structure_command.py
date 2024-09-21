from abc import abstractmethod, ABC
from typing import Optional
from collections import deque

class StructureCommand(ABC):
    @abstractmethod
    def execute(self, out: Optional[deque]):
        pass