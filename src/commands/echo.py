import glob
from commands.command import Command


class Echo(Command):

    def pre_process_args(self, args):
        expand = self.check_globbing(args)
        if expand:
            for index in expand:
                if expand[index]:
                    args = args[:index] + expand[index] + args[index + 1:]
        return args

    def execute(self, args, stdin=None):
        if args is None:
            return "\n"
        args = self.pre_process_args(args)

        return " ".join(args)

    @staticmethod
    def check_globbing(args):
        expand = {}
        for index, arg in enumerate(args):
            if "*" in arg:
                expanded_args = glob.glob(arg)
                expand[index] = expanded_args
        return expand
