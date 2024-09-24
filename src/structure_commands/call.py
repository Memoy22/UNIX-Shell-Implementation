from typing import Optional

from structure_commands.structure_command import StructureCommand
from command_factory import CommandFactory
from utils.validator import Validator
from utils.file import File


class Call(StructureCommand):
    def __init__(self, cmd: str, arguments: list[str], stdin: Optional[list[str]], stdout: Optional[list[str]]):
        self.cmd = cmd
        self.arguments = arguments
        self.stdin = stdin
        self.stdout = stdout
        self.pipe_flag = True

    def execute(self, out=None) -> Optional[str]:
        cmd = CommandFactory().get_command(self.cmd)

        # Read stdin if it is not from pipe
        if self.stdin is not None and self.pipe_flag:
            if self.cmd.startswith("_"):
                try:
                    self.stdin = self.read_stdin()
                except Exception as e:
                    out.append(f"{e}")
                    return f"{e}"
            else:
                self.stdin = self.read_stdin()

        res = cmd.execute(self.arguments, self.stdin)

        # If stdout is given, write and return early
        if self.stdout is not None:
            File.write(self.stdout, res)
            return

        if out is not None and res is not None:
            out.append(res)
            out.append("\n")
        return res

    def read_stdin(self) -> list[str]:
        Validator.check_path_exists(self.stdin)
        return File.read_lines(self.stdin)

    def __str__(self):
        return (f"Call(\n"
                f"    cmd={self.cmd},\n"
                f"    args={self.arguments},\n"
                f"    stdin={self.stdin},\n"
                f"    stdout={self.stdout}\n"
                f")")
