from commands.command import Command
from utils import Validator
from exceptions import FlagError
import os


class Ls(Command):

    def execute(self, args, stdin=None):
        path = self.validate_args(args)
        files = [file for file in os.listdir(path) if not file.startswith('.')]
        return '\t'.join(files) + '\n'

    @staticmethod
    def validate_args(args):
        """ Validate the arguments given in the command line.
        Args:
            args (list): List of arguments given in the command line.
        Returns:
            str: Path given in the command line.
        Raises:
            FlagError: If the number of flags given is not 1.
        """
        if args is None:
            return '.'
        num_args = len(args)
        if num_args == 1:
            Validator.check_path_exists(args[0])
            return args[0]
        else:
            raise FlagError("Error: Wrong number of flags given")
