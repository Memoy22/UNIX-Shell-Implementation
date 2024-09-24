from typing import Optional

from commands.command import Command
from utils.file import File
from utils.validator import Validator
from exceptions import FlagError


class Uniq(Command):

    def execute(self, args: list[str], stdin: Optional[list[str]] = None):
        case_insensitive, arguments = self.validate_args(args, stdin)
        lines = []
        for line in arguments:
            lines.extend(line.strip('\n').split('\n'))

        return '\n'.join(self.get_uniq(case_insensitive, lines))

    @staticmethod
    def validate_args(args, stdin) -> tuple[bool, list[str]]:
        """
        Raises:
            FlagError: If the flag given is not -i.
            FlagError: If the file does not exist.
        """
        num_args = 0 if args is None else len(args)
        case_insensitive = False
        if num_args == 0 and stdin is not None:
            lines = stdin
        elif num_args == 1:
            if args[0].startswith('-'):
                Validator.check_flag(args[0], "-i")
                case_insensitive = True
                lines = stdin
            else:
                Validator.check_path_exists(args[0])
                lines = File.read_lines(args[0])
        elif num_args == 2:
            Validator.check_flag(args[0], "-i")
            case_insensitive = True
            Validator.check_path_exists(args[1])
            lines = File.read_lines(args[1])
        else:
            raise FlagError("Error: Wrong number of flags given")
        return case_insensitive, lines

    @staticmethod
    def get_uniq(case_insensitive, lines) -> list[str]:
        """
        Get the unique lines from the given lines.
        """
        result_lines = []
        prev_line = None
        for line in lines:
            compare_line = line.lower() if case_insensitive else line
            if compare_line != prev_line:
                result_lines.append(line)
                prev_line = compare_line

        return result_lines
