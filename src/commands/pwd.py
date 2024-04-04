from commands.command import Command
import os


class Pwd(Command):
    def execute(self, args, stdIn=None):
        return os.getcwd()+'\n'
