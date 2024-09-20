import os
import unittest
from collections import deque
from exceptions import FlagError
from shell import eval


def get_result(out, split_type="\n"):
    result = []
    while out:
        result.append(out.popleft())
    return "".join(result).strip().split(split_type)


class TestCd(unittest.TestCase):
    test_files_dir = "test/test_files"

    file1 = "test/test_files/file1.txt"
    file2 = "test/test_files/file2.txt"
    empty = "test/test_files/empty.txt"

    file1_content = ["Lorem", "Ipsum", "Dolor"]
    file2_content = ["ABCD", "EFGH", "IJKL", "MNOP"]
    empty_content = [""]

    def test_cd_change_dir(self, out=deque()):
        eval(f"cd {self.test_files_dir}; echo *.txt", out)

        # To come to comp0010 directory for other tests
        eval("cd /comp0010", out)

        result = get_result(out, " ")
        result = set(result)
        self.assertEqual(
            result,
            {
                "file2.txt",
                "empty.txt",
                "file1.txt",
                "out.txt"
            }
        )

    def test_cd_non_existing_dir(self, out=deque()):
        with self.assertRaises(FlagError):
            eval("cd nonExistingDirectory/", out)

    def test_cd_no_args(self, out=deque()):
        eval("cd; pwd", out)
        result = get_result(out)
        self.assertEqual(result, [os.getcwd()])
