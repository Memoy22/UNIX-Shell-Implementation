import unittest
from collections import deque
from exceptions import CommandNotFoundError
from shell import eval


def get_result(out, split_type="\n"):
    result = []
    while out:
        result.append(out.popleft())
    return "".join(result).strip().split(split_type)


class TestShell(unittest.TestCase):
    test_files_dir = "test/test_files"

    file1 = "test/test_files/file1.txt"
    file2 = "test/test_files/file2.txt"
    empty = "test/test_files/empty.txt"

    file1_content = ["Lorem", "Ipsum", "Dolor"]
    file2_content = ["ABCD", "EFGH", "IJKL", "MNOP"]
    empty_content = [""]

    def test_empty_cmdline(self, out=deque()):
        eval("", out)
        result = get_result(out)
        self.assertEqual(result, [""])

    def test_unsafe_command_not_exists(self, out=deque()):
        with self.assertRaises(CommandNotFoundError):
            eval("_wrong", out)


if __name__ == "__main__":
    unittest.main()
