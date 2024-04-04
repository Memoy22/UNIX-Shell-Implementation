import re

from commands.command import Command
from exceptions import FlagError
from utility import File, Validator


class Grep(Command):
    def execute(self, args, stdIn=None):
        """ Execute the grep command.
        Args:
            args (list): List of arguments given in the command line.
            stdIn (list): List of lines from standard input.
        Returns:
            str: Lines that match the pattern.
        Raises:
            FlagError: If the number of flags given is not 1.
            FlagError: If the file does not exist.
        """
        match_lines = []
        if args:
            pattern = args[0]
            files = args[1:]
        if not args and stdIn is None:
            raise FlagError("Error: Wrong number of flags given")

        if args and files:
            multi_files = True if len(files) > 1 else False
            for file in files:
                Validator.check_path_exists(file)
                lines = File(file).read_lines()
                lines = [line.rstrip() for line in lines]
                for line in lines:
                    if re.search(pattern, line):
                        match_lines.append(file + ":" +
                                           line if multi_files else line)
        elif stdIn is not None:
            stdIn = [line.rstrip() for line in stdIn]
            for line in stdIn:
                if re.search(pattern, line):
                    match_lines.append(line)

        return "\n".join(match_lines) + "\n"
