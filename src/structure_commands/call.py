from commands.command import Command
from typing import Optional
from collections import deque


class Call:
    def __init__(self, cmd=None, arguments=None, stdin=None, stdout=None):
        self.cmd = cmd
        self.arguments = arguments if arguments is not None else []
        self.stdin = stdin
        self.stdout = stdout

    def eval(self, input_cmd: Optional[str], out: deque):
        # Simulate command evaluation (this can be customized)
        out.append(' '.join(self.arguments))

    def __repr__(self):
        return f"Call(cmd={self.cmd}, args={self.arguments} stdin={self.stdin} stdout={self.stdout})"