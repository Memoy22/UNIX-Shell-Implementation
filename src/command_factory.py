from commands.cat import Cat
from commands.cd import Cd
from commands.cut import Cut
from commands.echo import Echo
from commands.find import Find
from commands.grep import Grep
from commands.head import Head
from commands.ls import Ls
from commands.mkdir import Mkdir
from commands.pwd import Pwd
from commands.sort import Sort
from commands.tail import Tail
from commands.uniq import Uniq
from commands.wc import Wc
from exceptions import CommandNotFoundError


class CommandFactory:
    """
    Factory class for commands.
    This class is responsible for creating command objects.
    """
    def __init__(self):
        self.command_factory = {
            "pwd": Pwd,
            "echo": Echo,
            "ls": Ls,
            "cd": Cd,
            "cat": Cat,
            "head": Head,
            "tail": Tail,
            "grep": Grep,
            "find": Find,
            "sort": Sort,
            "uniq": Uniq,
            "cut": Cut,
            "wc": Wc,
            "mkdir": Mkdir
        }

    def get_command(self, cmd):
        cmd_obj = self.command_factory.get(cmd)
        if cmd_obj is None:
            raise CommandNotFoundError("Error: Command Not Found")
        return cmd_obj()

    def is_command(self, cmd):
        return cmd in self.command_factory
