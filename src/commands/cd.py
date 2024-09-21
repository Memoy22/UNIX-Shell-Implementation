from commands.command import Command
from utils.validator import Validator
from typing import Optional
import os


class Cd(Command):
    def execute(self, args: list[str], stdin: Optional[list[str]]=None) ->None:
        if args:
            Validator.check_path_exists(args[0])
            os.chdir(args[0])
