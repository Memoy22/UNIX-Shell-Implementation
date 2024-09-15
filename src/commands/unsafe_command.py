from commands.command import Command


class UnsafeDecorator(Command):
    def __init__(self, cmd):
        self.unsafe_cmd = cmd

    def execute(self, args, stdin):
        try:
            return self.unsafe_cmd.execute(args, stdin)
        except Exception as e:
            return str(e)
