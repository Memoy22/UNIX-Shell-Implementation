from structure_commands.structure_command import StructureCommand
from structure_commands.call import Call


class Seq(StructureCommand):
    def __init__(self, left: Call, right: Call):
        self.left = left
        self.right = right

    def execute(self, out=None) -> list[str]:
        left = self.left.execute(out)
        right = self.right.execute(out)

        # return left and right calls for nested structure commands
        return [left, right]

    def __repr__(self):
        return f"Seq(left={self.left}, right={self.right})"
