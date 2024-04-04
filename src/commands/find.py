from commands.command import Command
from exceptions import FlagError
from utils import Validator
import os
import fnmatch


class Find(Command):

    def execute(self, args, stdin=None):
        path, pattern = self.validate_flags(args)
        matched_files = self.find_files(path, pattern)
        return '\n'.join(matched_files) + '\n'

    @staticmethod
    def validate_flags(args):
        """ Validate the flags given in the command line.
        Args:
            args (list): List of arguments given in the command line.
        Returns:
            tuple: Tuple containing the path and pattern to search for.
        Raises:
            FlagError: If the number of flags given is not 2 or 3.
            FlagError: If the flag given is not -name.
            FlagError: If the path does not exist.
        """
        num_args = len(args)
        if num_args == 2:
            path = '.'
            Validator.check_flag(args[0], "-name")
            pattern = args[-1]
        elif num_args == 3:
            path = args[0]
            Validator.check_path_exists(path)
            Validator.check_flag(args[1], "-name")
            pattern = args[2]
        else:
            raise FlagError("Error: Wrong number of flags given")
        return path, pattern

    @staticmethod
    def find_files(path, pattern):
        """ Find files in the given path that match the pattern.
        Args:
            path (str): Path to search for files.
            pattern (str): Pattern to search for.
        Returns:
            generator: Generator containing the files that match the pattern.
        """
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in fnmatch.filter(filenames, pattern):
                yield os.path.join(dirpath, filename)
