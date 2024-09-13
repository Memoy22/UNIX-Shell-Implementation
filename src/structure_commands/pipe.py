from commands.command import Command
from typing import Optional
from collections import deque


class Pipe:
    def __init__(self, left: Command, right: Command):
        super().__init__()
        self.left = left
        self.right = right

    def eval(self, input_cmd: Optional[str], out: deque):
        # Simulate pipe evaluation
        temp_out = deque()
        for command in self.commands:
            command.eval(input_cmd, temp_out)
        # Piped commands accumulate results, so we append the final output.
        out.append(' | '.join(temp_out))

    def __repr__(self):
        return f"Pipe(left={self.left} right={self.right})"
