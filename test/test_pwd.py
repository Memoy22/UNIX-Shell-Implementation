import os
import unittest
from collections import deque
from shell import eval
from utils.file import File


def get_result(out, split_type="\n"):
    result = []
    while out:
        result.append(out.popleft())
    return "".join(result).strip().split(split_type)


class TestPwd(unittest.TestCase):
    test_files_dir = "test/test_files"

    file1 = "test/test_files/file1.txt"
    file2 = "test/test_files/file2.txt"
    empty = "test/test_files/empty.txt"

    file1_content = ["Lorem", "Ipsum", "Dolor"]
    file2_content = ["ABCD", "EFGH", "IJKL", "MNOP"]
    empty_content = [""]

    out_dir = "test/test_files/out.txt"

    def test_pwd(self, out=deque()):
        eval("pwd", out)
        result = get_result(out)
        self.assertEqual(result, os.getcwd().strip().split("\n"))

    def test_pwd_redir_out(self, out=deque()):
        eval(f"pwd > {self.out_dir}", out)
        result = File.read(self.out_dir).strip().split("\n")
        self.assertEqual(result, os.getcwd().strip().split("\n"))
