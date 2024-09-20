import unittest
from collections import deque
from exceptions import FlagError
from shell import eval


def get_result(out, split_type="\n"):
    result = []
    while out:
        result.append(out.popleft())
    return "".join(result).strip().split(split_type)


class TestTail(unittest.TestCase):
    test_files_dir = "test/test_files"

    file1 = "test/test_files/file1.txt"
    file2 = "test/test_files/file2.txt"
    empty = "test/test_files/empty.txt"

    file1_content = ["Lorem", "Ipsum", "Dolor"]
    file2_content = ["ABCD", "EFGH", "IJKL", "MNOP"]
    empty_content = [""]

    def test_tail_stdIn(self, out=deque()):
        eval(f"tail < {self.file1}", out)
        result = get_result(out)
        self.assertEqual(result, self.file1_content)

    def test_tail_default_n(self, out=deque()):
        eval(f"tail {self.file1}", out)
        result = get_result(out)
        self.assertEqual(result, self.file1_content)

    def test_tail_too_many_args(self, out=deque()):
        with self.assertRaises(FlagError):
            eval(f"tail -n -j 3 {self.file1}", out)
