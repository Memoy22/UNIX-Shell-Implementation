from structure_commands.structure_command import StructureCommand
from structure_commands.call import Call


class Pipe(StructureCommand):
    def __init__(self, left: Call, right: Call):
        self.left = left
        self.right = right

    def execute(self, out=None) -> str:

        res = self.left.execute()

        # Only assign pipe to stdin if no prior stdin is given
        if self.right.stdin is None:
            self.right.stdin = [res]

            # Set to false so that call does not read stdin as it is not a file
            self.right.pipe_flag = False

        # return right call result for nested structure commands
        return self.right.execute(out)

    def __str__(self):
        left_str = str(self.left).replace("\n", "\n    ")
        right_str = str(self.right).replace("\n", "\n    ")

        return (f"Pipe(\n"
                f"    left={left_str},\n"
                f"    right={right_str}\n"
                f")")
