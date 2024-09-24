from structure_commands.structure_command import StructureCommand
from structure_commands.call import Call


class Seq(StructureCommand):
    def __init__(self, left: Call, right: Call):
        self.left = left
        self.right = right

    def execute(self, out=None) -> list[str]:
        left = self.left.execute(out)
        right = self.right.execute(out)

        # return left and right calls for substituted seq structure commands
        return [left, right]

    def __str__(self):
        left_str = str(self.left).replace("\n", "\n    ")
        right_str = str(self.right).replace("\n", "\n    ")

        return (f"Seq(\n"
                f"    left={left_str},\n"
                f"    right={right_str}\n"
                f")")
