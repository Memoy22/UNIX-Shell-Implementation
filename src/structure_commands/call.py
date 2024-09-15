from commands.command import Command
from command_factory import CommandFactory
from utils import Validator, File


class Call(Command):
    def __init__(self, cmd=None, arguments=None, stdin=None, stdout=None):
        self.cmd = cmd
        self.arguments = arguments
        self.stdin = stdin
        self.stdout = stdout
        self.pipe_flag = True

    def execute(self, out=None):
        cmd = CommandFactory().get_command(self.cmd)

        if self.stdin is not None and self.pipe_flag:
            Validator.check_path_exists(self.stdin)
            self.stdin = File(self.stdin).read_lines()

        res = cmd.execute(self.arguments, self.stdin)

        if self.stdout is not None:
            File(self.stdout).write(res)
            return

        if out is not None and res is not None:
            out.append(res)
            out.append("\n")
        return res

    def __repr__(self):
        return f"Call(cmd={self.cmd}, args={self.arguments} stdin={self.stdin} stdout={self.stdout})"
