from typing import Optional

from commands.command import Command
from utils.file import File
from utils.validator import Validator
from exceptions import FlagError


class Sort(Command):

    def execute(self, args: list[str], stdin: Optional[list[str]]=None) -> str :
        rev, arguments = self.validate_args(args, stdin)
        lines = []
        for line in arguments:
            lines.extend(line.strip('\n').split('\n'))

        sorted_lines = sorted(lines, reverse=rev)
        return '\n'.join(sorted_lines)

    @staticmethod
    def validate_args(args, stdin) -> tuple[bool, list[str]]:
        """
        Raises:
            FlagError: If the flag given is not -r.
            FlagError: If the file does not exist.
        """
        num_args = 0 if args is None else len(args)
        rev = False
        if num_args == 0 and stdin is not None:
            lines = stdin
        elif num_args == 1:
            if args[0].startswith('-'):
                Validator.check_flag(args[0], "-r")
                rev = True
                lines = stdin
            else:
                Validator.check_path_exists(args[0])
                lines = File.read_lines(args[0])
        elif num_args == 2:
            Validator.check_flag(args[0], "-r")
            rev = True
            Validator.check_path_exists(args[1])
            lines = File.read_lines(args[1])
        else:
            raise FlagError("Error: Wrong number of flags given")
        return rev, lines
