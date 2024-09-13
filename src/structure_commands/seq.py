from commands.command import Command
from typing import Optional
from collections import deque


class Seq:
    def __init__(self, left: Command, right: Command):
        super().__init__()
        self.left = left
        self.right = right

    def __eq__(self, other):
        return isinstance(other,
                          Seq) and self.left == other.left and self.right == other.right

    def eval(self, input_cmd: Optional[str], out: deque):
        # Left and right are evaluated separately
        self.left.eval(input_cmd, out)
        self.right.eval(None, out)

    def __repr__(self):
        return f"Seq(left={self.left}, right={self.right})"
