from typing import Optional

from commands.command import Command
from exceptions import FlagError
from utils.file import File
from utils.validator import Validator


class Wc(Command):

    def execute(self, args: list[str], stdin: Optional[list[str]]=None) -> str:
        """
        Execute the wc command:
        -l: counts lines
        -w: counts words (separated by whitespaces)
        -m: counts characters (including whitespaces and newlines)
        """
        temp = self.validate_args(args, stdin)
        flags = temp[0]
        lines = temp[1]

        output = []

        if flags[0]:
            output.append(str(self.exec_l(lines)))
        if flags[1]:
            output.append(str(self.exec_w(lines)))
        if flags[2]:
            output.append(str(self.exec_m(lines)))

        return " ".join(output)

    def validate_args(self, args, stdin) -> tuple[tuple[bool, bool, bool], list[str]]:
        """
        Raises:
            FlagError: If the flag given is not -l, -w, or -m.
            FlagError: If the file does not exist.
            FlagError: If the wrong number of arguments are given
        """
        l, w, m = True, True, True
        num_args = len(args) if args else 0
        if num_args == 0 and stdin is not None:
            lines = stdin
        elif num_args > 0:
            if args[0].startswith("-"):
                l, w, m = self.validate_flags(args[0])
                lines = self.validate_files(args[1:])
                if not lines:
                    lines = stdin
            else:
                lines = self.validate_files(args)
        else:
            raise FlagError("Error: Wrong number of arguments given")

        return (l, w, m), lines

    @staticmethod
    def validate_flags(arg) -> tuple[bool, bool, bool]:
        """
        Validate the flags given in the command line
        Raises:
            FlagError: If the flag given is not -l, -w, or -m.
        """
        l_flag, w_flag, m_flag = False, False, False
        if arg == "-l":
            l_flag = True
        elif arg == "-w":
            w_flag = True
        elif arg == "-m":
            m_flag = True
        else:
            msg = "Error: Wrong flag name given."
            msg2 = f"Expected: -l,-w,-m Given: '{arg}'"
            raise FlagError(msg + " " + msg2)
        return l_flag, w_flag, m_flag

    @staticmethod
    def validate_files(files) -> list[str]:
        """
        Validate the files by checking path and reading them.
        Raises:
            FlagError: If the file does not exist.
        """
        for file in files:
            Validator.check_path_exists(file)
        lines = []
        for file in files:
            temp_lines = File.read_lines(file)
            lines += temp_lines
        return lines

    @staticmethod
    def exec_l(lines):
        return len(lines)

    @staticmethod
    def exec_w(lines) -> int:
        words = 0
        for line in lines:
            temp_words = len(line.split(" "))
            words += temp_words
        return words

    @staticmethod
    def exec_m(lines) -> int:
        chars = 0
        for line in lines:
            temp_chars = len(line)
            chars += temp_chars
        return chars
