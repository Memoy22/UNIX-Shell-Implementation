import os

from commands.command import Command
from exceptions import FileAlreadyExistsError
from exceptions import FlagError
from utility import Validator


class Mkdir(Command):
    @staticmethod
    def raise_error(file):
        msg = f"Error: Cannot create directory. '{file}' already exists"
        raise FileAlreadyExistsError(msg)

    @staticmethod
    def validate_args(args):
        """ Validate the arguments given in the command line.
        Args:
            args (list): List of arguments given in the command line.
        Returns:
            tuple: Tuple containing the flags and directories.
        Raises:
            FlagError: If the flag given is not -p.
            FlagError: If the directory already exists.
            FlagError: If the flag -p is not given.
        """
        num_args = len(args) if args else 0
        p = False
        if num_args == 0:
            raise FlagError("Error: mkdir: Operand missing")
        elif num_args == 1:
            if args[0].startswith('-'):
                Validator.check_flag(args[0], "-p")
                raise FlagError("Error: mkdir: Operand missing")
            else:
                dirs = args
        else:
            if args[0].startswith('-'):
                Validator.check_flag(args[0], "-p")
                p = True
                dirs = args[1:]
        return p, dirs

    def execute(self, args, stdIn):
        p, dirs = self.validate_args(args)
        for dir in dirs:
            if Validator.check_path_exists_bool(dir):
                self.raise_error(dir)
            if p:
                os.makedirs(dir)
            else:
                try:
                    os.mkdir(dir)
                except FileNotFoundError:
                    raise FlagError(f"Error: Flag -p required for '{dir}'")
