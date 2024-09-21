from commands.command import Command
from structure_commands.call import Call


class Seq(Command):
    def __init__(self, left: Call, right: Call):
        self.left = left
        self.right = right

    def execute(self, out=None):
        left = self.left.execute(out)
        right = self.right.execute(out)
        return [left, right]

    def __repr__(self):
        return f"Seq(left={self.left}, right={self.right})"
