import unittest
from collections import deque
from exceptions import (FlagError, FileAlreadyExistsError)
from shell import eval


def get_result(out, split_type="\n"):
    result = []
    while out:
        result.append(out.popleft())
    return "".join(result).strip().split(split_type)


class TestWc(unittest.TestCase):
    test_files_dir = "test/test_files"

    file1 = "test/test_files/file1.txt"
    file2 = "test/test_files/file2.txt"
    empty = "test/test_files/empty.txt"

    file1_content = ["Lorem", "Ipsum", "Dolor"]
    file2_content = ["ABCD", "EFGH", "IJKL", "MNOP"]
    empty_content = [""]

    def test_mkdir(self, out=deque()):
        eval("mkdir mkdir_test; ls", out)
        result = get_result(out, "\t")
        self.assertTrue("mkdir_test" in result)

    def test_mkdir_multiple(self, out=deque()):
        eval("mkdir -p mkdir_test1 mkdir_test2; ls", out)
        result = get_result(out, "\t")
        self.assertTrue({'mkdir_test1', 'mkdir_test2'}.issubset(result))

    def test_mkdir_already_exists(self, out=deque()):
        with self.assertRaises(FileAlreadyExistsError):
            eval("mkdir test", out)

    def test_mkdir_missing_operand(self, out=deque()):
        with self.assertRaises(FlagError):
            eval("mkdir", out)

    def test_mkdir_p(self, out=deque()):
        with self.assertRaises(FlagError):
            eval("mkdir -p", out)

    def test_mkdir_missing_p(self, out=deque()):
        with self.assertRaises(FlagError):
            eval("mkdir a/b", out)
