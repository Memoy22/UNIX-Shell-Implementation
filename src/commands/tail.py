from typing import Optional

from commands.command import Command
from utils.file import File
from utils.validator import Validator
from exceptions import FlagError


class Tail(Command):

    def execute(self, args: list[str], stdin: Optional[list[str]] = None):
        n, lines = self.validate_flags(args, stdin)
        if n == 0:
            return '\n'

        tail_lines = lines[-n:]
        return '\n'.join(tail_lines)

    @staticmethod
    def validate_flags(args, stdin) -> tuple[int, list[str]]:
        """
        Raises:
            FlagError: If the flag given is not -n.
            FlagError: If the file does not exist.
        """
        num_args = len(args) if args else 0
        n = 10
        if num_args == 0 and stdin is not None:
            lines = [
                item for line in stdin for item in line.split("\n") if item
            ]
        elif num_args == 1:
            Validator.check_path_exists(args[0])
            lines = File.read_lines(args[0])
            lines = [line.rstrip('\n') for line in lines]
        elif num_args == 2:
            Validator.check_flag(args[0], "-n")
            Validator.check_string_isdigit(args[1])
            n = int(args[1])
            lines = [
                item for line in stdin for item in line.split("\n") if item
            ]
        elif num_args == 3:
            Validator.check_flag(args[0], "-n")
            Validator.check_string_isdigit(args[1])
            n = int(args[1])
            Validator.check_path_exists(args[2])
            lines = File.read_lines(args[2])
            lines = [line.rstrip('\n') for line in lines]
        else:
            raise FlagError("Error: Wrong number of flags given")
        return n, lines
