from commands.command import Command
from utils import File
from utils import Validator


class Cat(Command):
    def execute(self, args, stdin=None):
        """ Concatenate files and print on the standard output.
        Args:
            args (list): List of arguments given in the command line.
            stdin (list): List of lines from standard input.
        Returns:
            str: Concatenated output of files or standard input.
        Raises:
            FileNotFoundError: If the file does not exist.
        """
        concat_output = []
        if args:
            for file_path in args:
                Validator.check_path_exists(file_path)
                concat_output.append(File(file_path).read())
        elif stdin is not None:
            for line in stdin:
                concat_output += line

        return "".join(concat_output)
