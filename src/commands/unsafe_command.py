from typing import Optional

from commands.command import Command


class UnsafeDecorator(Command):
    def __init__(self, cmd: Command):
        self.unsafe_cmd = cmd

    def execute(self, args: list[str], stdin: Optional[str]) -> str:
        try:
            return self.unsafe_cmd.execute(args, stdin)
        except Exception as e:
            return str(e)
