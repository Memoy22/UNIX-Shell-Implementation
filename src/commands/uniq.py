from commands.command import Command
from src.utils.file import File
from src.utils.validator import Validator
from exceptions import FlagError


class Uniq(Command):

    def execute(self, args, stdin=None):
        case_insensitive, arguments = self.validate_args(args, stdin)
        lines = []
        for line in arguments:
            lines.extend(line.strip('\n').split('\n'))

        return '\n'.join(self.get_uniq(case_insensitive, lines))

    @staticmethod
    def validate_args(args, stdin):
        """
        Validate the arguments given in the command line.
        Args:
            args (list): List of arguments given in the command line.
            stdin (list): List of lines from standard input.
        Returns:
            tuple: Tuple containing the flags and lines from files or stdin.
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
    def get_uniq(case_insensitive, lines):
        """ Get the unique lines from the given lines.
        Args:
            case_insensitive (bool): Flag to ignore case.
            lines (list): List of lines to get unique lines from.
        Returns:
            list: List of unique lines.
        """
        result_lines = []
        prev_line = None
        for line in lines:
            compare_line = line.lower() if case_insensitive else line
            if compare_line != prev_line:
                result_lines.append(line)
                prev_line = compare_line

        return result_lines
