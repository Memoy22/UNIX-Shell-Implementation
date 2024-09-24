from typing import Optional, Generator

from commands.command import Command
from exceptions import FlagError
from utils.validator import Validator
import os
import fnmatch


class Find(Command):

    def execute(self, args: list[str], stdin: Optional[list[str]] = None):
        path, pattern = self.validate_flags(args)
        matched_files = self.find_files(path, pattern)
        return '\n'.join(matched_files)

    @staticmethod
    def validate_flags(args) -> tuple[str, str]:
        """
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
    def find_files(path: str, pattern: str) -> Generator[str, None, None]:
        """
        Find files in the given path that match the pattern.
        """
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in fnmatch.filter(filenames, pattern):
                yield os.path.join(dirpath, filename)
