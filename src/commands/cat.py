from commands.command import Command
from utils.file import File
from utils.validator import Validator
from typing import Optional


class Cat(Command):
    def execute(self, args: list[str], stdin: Optional[list[str]] = None):
        concat_output = []
        if args:
            for file_path in args:
                Validator.check_path_exists(file_path)
                concat_output.append(File.read(file_path))
        elif stdin is not None:
            for line in stdin:
                concat_output += line

        return "".join(concat_output)
