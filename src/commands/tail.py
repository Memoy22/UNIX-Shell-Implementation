from commands.command import Command
from utility import File
from utility import Validator
from exceptions import FlagError


class Tail(Command):
    @staticmethod
    def validate_flags(args, stdIn):
        """
        Validate the flags given in the command line.
        Args:
            args (list): List of arguments given in the command line.
            stdIn (list): List of lines from standard input.
        Returns:
            tuple: Tuple containing the number of lines and lines from files or standard input.
        Raises:
            FlagError: If the flag given is not -n.
            FlagError: If the file does not exist.
        """
        num_args = len(args) if args else 0
        n = 10
        if num_args == 0 and stdIn is not None:
            lines = stdIn
        elif num_args == 1:
            Validator.check_path_exists(args[0])
            lines = File(args[0]).read_lines()
        elif num_args == 2:
            Validator.check_flag(args[0], "-n")
            Validator.check_string_isdigit(args[1])
            n = int(args[1])
            lines = stdIn
        elif num_args == 3:
            Validator.check_flag(args[0], "-n")
            Validator.check_string_isdigit(args[1])
            n = int(args[1])
            Validator.check_path_exists(args[2])
            lines = File(args[2]).read_lines()
        else:
            raise FlagError("Error: Wrong number of flags given")
        return n, lines

    def execute(self, args, stdIn=None):
        n, lines = self.validate_flags(args, stdIn)
        if n == 0:
            return '\n'

        lines = [line.rstrip('\n') for line in lines]
        tail_lines = lines[-n:]
        return '\n'.join(tail_lines) + '\n'
