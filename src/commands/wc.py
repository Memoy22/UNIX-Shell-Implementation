from commands.command import Command
from exceptions import FlagError
from src.utils.file import File
from src.utils.validator import Validator


class Wc(Command):

    def validate_args(self, args, stdin):
        """
        Validate the arguments given in the command line.
        Args:
            args (list): List of arguments given in the command line.
            stdin (list): List of lines from standard input.
        Returns:
            tuple: Tuple containing the flags and lines from files or stdin.
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
                l, w, m = self.process_flag(args[0])
                lines = self.process_files(args[1:])
                if not lines:
                    lines = stdin
            else:
                lines = self.process_files(args)
        else:
            raise FlagError("Error: Wrong number of arguments given")

        return (l, w, m), lines

    def execute(self, args, stdin):
        """ Execute the wc command.
        Args:
            args (list): List of arguments given in the command line.
            stdin (list): List of lines from standard input.
        Returns:
            str: The output of the wc command.
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

    @staticmethod
    def process_flag(arg):
        """
        Process the flag given in the command line.
        Args:
            arg (str): Flag given in the command line.
        Returns:
            tuple: Tuple containing the flags for l, w, m.
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
    def process_files(files):
        """
        Process the files by checking path and reading them.
        Args:
            files (list): List of files given in the command line.
        Returns:
            list: List of lines from all the files.
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
    def exec_w(lines):
        words = 0
        for line in lines:
            temp_words = len(line.split(" "))
            words += temp_words
        return words

    @staticmethod
    def exec_m(lines):
        chars = 0
        for line in lines:
            temp_chars = len(line)
            chars += temp_chars
        return chars
