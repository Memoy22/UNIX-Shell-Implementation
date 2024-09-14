from commands.command import Command
from command_factory import CommandFactory


class Call(Command):
    def __init__(self, cmd=None, arguments=None, stdin=None, stdout=None):
        self.cmd = cmd
        self.arguments = arguments
        self.stdin = stdin
        self.stdout = stdout

    def execute(self, out=None):
        cmd = CommandFactory().get_command(self.cmd)
        res = cmd.execute(self.arguments, self.stdin)
        if out is not None:
            out.append(res)
            return
        return res

    def __repr__(self):
        return f"Call(cmd={self.cmd}, args={self.arguments} stdin={self.stdin} stdout={self.stdout})"
