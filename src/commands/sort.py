from commands.command import Command
from utility import File
from utility import Validator
from exceptions import FlagError


class Sort(Command):
    @staticmethod
    def validate_args(args, stdIn):
        """ Validate the arguments given in the command line.
        Args:
            args (list): List of arguments given in the command line.
            stdIn (list): List of lines from standard input.
        Returns:
            tuple: Tuple containing the flags and lines from files or standard input.
        Raises:
            FlagError: If the flag given is not -r.
            FlagError: If the file does not exist.
        """
        num_args = 0 if args is None else len(args)
        rev = False
        if num_args == 0 and stdIn is not None:
            lines = stdIn
        elif num_args == 1:
            if args[0].startswith('-'):
                Validator.check_flag(args[0], "-r")
                rev = True
                lines = stdIn
            else:
                Validator.check_path_exists(args[0])
                lines = File(args[0]).read_lines()
        elif num_args == 2:
            Validator.check_flag(args[0], "-r")
            rev = True
            Validator.check_path_exists(args[1])
            lines = File(args[1]).read_lines()
        else:
            raise FlagError("Error: Wrong number of flags given")
        return rev, lines

    def execute(self, args, stdIn=None):
        rev, lines = self.validate_args(args, stdIn)
        lines = [line.rstrip('\n') for line in lines]
        sorted_lines = sorted(lines, reverse=rev)
        return '\n'.join(sorted_lines)+'\n'
