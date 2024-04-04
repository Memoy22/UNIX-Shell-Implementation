from commands.command import Command
from utility import File
from utility import Validator


class Cat(Command):
    def execute(self, args, stdIn=None):
        """ Concatenate files and print on the standard output.
        Args:
            args (list): List of arguments given in the command line.
            stdIn (list): List of lines from standard input.
        Returns:
            str: Concatenated output of files or standard input.
        Raises:
            FileNotFoundError: If the file does not exist.
        """
        concat_output = ""
        if args:
            for file_path in args:
                Validator.check_path_exists(file_path)
                concat_output += File(file_path).read()
        elif stdIn is not None:
            for line in stdIn:
                concat_output += line

        return concat_output + "\n"
