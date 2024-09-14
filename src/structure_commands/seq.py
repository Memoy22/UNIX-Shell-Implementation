from commands.command import Command
from structure_commands.call import Call
from collections import deque


class Seq(Command):
    def __init__(self, left: Call, right: Call):
        self.left = left
        self.right = right

    def execute(self, out):
        self.left.execute(out)
        self.right.execute(out)

    def __repr__(self):
        return f"Seq(left={self.left}, right={self.right})"
