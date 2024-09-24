from typing import Optional

from commands.command import Command
import os


class Pwd(Command):
    def execute(self, args: list[str], stdin: Optional[list[str]] = None):
        return os.getcwd()
