import os

from exceptions import FlagError, FlagValueError


class File:
    """
    Class to read and write to files.
    Args:
        file (str): Path to the file.
    Methods:
        read_lines: Read all lines from the file and store in list.
        read: Read the entire file and store in string.
        write: Write to the file.
    """
    def __init__(self, file):
        self.file = file

    def read_lines(self):
        with open(self.file, "r") as fin:
            lines = fin.readlines()
        return lines

    def read(self):
        with open(self.file, "r") as fin:
            line = fin.read()
        return line

    def write(self, output):
        with open(self.file, "w") as fout:
            fout.write(output)
        return


class Validator:
    """
    Class to validate flags and paths.
    Methods:
        check_flag: Check if the given flag is the expected flag.
        check_path_exists: Check if the given path exists.
        check_path_exists_bool: Check if given path exists and return a boolean
        check_string_isdigit: Check if the given string is a digit.
    """
    @staticmethod
    def check_flag(given_flag, actual_flag):
        msg = "Error: Wrong flag name given."
        msg2 = f"Expected: '{actual_flag}' Given: '{given_flag}'"
        if given_flag != actual_flag:
            raise FlagError(msg + " " + msg2)

    @staticmethod
    def check_path_exists(path):
        if not os.path.exists(path):
            raise FlagError(f"Error: '{path}': No such file or directory")

    @staticmethod
    def check_path_exists_bool(path):
        return os.path.exists(path)

    @staticmethod
    def check_string_isdigit(char):
        msg = "Invalid flag argument. Expected digit(s)"
        if not char.isdigit():
            raise FlagValueError(msg)
