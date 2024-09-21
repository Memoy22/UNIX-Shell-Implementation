from commands.command import Command
from src.utils.file import File
from src.utils.validator import Validator
from exceptions import FlagError


class Sort(Command):

    def execute(self, args, stdin=None):
        rev, arguments = self.validate_args(args, stdin)
        lines = []
        for line in arguments:
            lines.extend(line.strip('\n').split('\n'))

        sorted_lines = sorted(lines, reverse=rev)
        return '\n'.join(sorted_lines)

    @staticmethod
    def validate_args(args, stdin):
        """ Validate the arguments given in the command line.
        Args:
            args (list): List of arguments given in the command line.
            stdin (list): List of lines from standard input.
        Returns:
            tuple: Tuple containing the rev flag and lines from files or stdin.
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
