import glob
from typing import Optional

from commands.command import Command


class Echo(Command):

    def execute(self, args: list[str], stdin: Optional[list[str]] = None):
        if args is None:
            return "\n"
        args = self.pre_process_globbing_in_args(args)

        return " ".join(args)

    def pre_process_globbing_in_args(self, args) -> list[str]:
        expand = self.check_globbing(args)
        if expand:
            for index in expand:
                if expand[index]:
                    args = args[:index] + expand[index] + args[index + 1:]
        return args

    @staticmethod
    def check_globbing(args) -> dict[int, list[str]]:
        expand = {}
        for index, arg in enumerate(args):
            if "*" in arg:
                expanded_args = glob.glob(arg)
                expand[index] = expanded_args
        return expand
