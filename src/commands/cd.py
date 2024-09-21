from commands.command import Command
from src.utils.validator import Validator
import os


class Cd(Command):
    def execute(self, args, stdin=None):
        if args:
            Validator.check_path_exists(args[0])
            os.chdir(args[0])
