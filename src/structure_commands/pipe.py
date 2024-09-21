from commands.command import Command
from structure_commands.call import Call


class Pipe(Command):
    def __init__(self, left: Call, right: Call):
        self.left = left
        self.right = right

    def execute(self, out=None):

        res = self.left.execute()
        if self.right.stdin is None:
            self.right.stdin = [res]
            self.right.pipe_flag = False

        return self.right.execute(out)

    def __repr__(self):
        return f"Pipe(left={self.left} right={self.right})"
