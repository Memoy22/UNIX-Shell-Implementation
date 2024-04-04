from commands.command import Command
import os


class Pwd(Command):
    def execute(self, args, stdin=None):
        return os.getcwd()+'\n'
