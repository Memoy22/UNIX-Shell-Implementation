import unittest
from collections import deque
from parameterized import parameterized
from exceptions import FlagError
from shell import eval
from utils import File


def get_result(out, split_type="\n"):
    result = []
    while out:
        result.append(out.popleft())
    return "".join(result).strip().split(split_type)


class TestLs(unittest.TestCase):
    test_files_dir = "test/test_files"

    file1 = "test/test_files/file1.txt"
    file2 = "test/test_files/file2.txt"
    empty = "test/test_files/empty.txt"

    file1_content = ["Lorem", "Ipsum", "Dolor"]
    file2_content = ["ABCD", "EFGH", "IJKL", "MNOP"]
    empty_content = [""]

    out_dir = "test/test_files/out.txt"

    @parameterized.expand(
        [
            # Directory containing file and folders
            (
                    "test/test_files",
                    [
                        "dir1",
                        "file2.txt",
                        "empty.txt",
                        "file1.txt",
                        "out.txt"
                    ]
            ),
            # Directory containing file with name starting with '.'
            ("test/test_files/dir1/dir1_subdir2", ["file.csv"]),
        ]
    )
    def test_ls(self, directory, expected_result, out=deque()):
        eval(f"ls {directory}", out)
        result = get_result(out, "\t")
        result = set(result)
        self.assertEqual(result, set(expected_result))

    def test_ls_dir_not_exists(self, out=deque()):
        with self.assertRaises(FlagError):
            eval("ls notExistsDir", out)

    def test_ls_redir_in(self, out=deque()):
        eval(f"ls test/test_files > {self.out_dir}", out)
        result = File(self.out_dir).read().strip().split("\t")
        expected = {"dir1", "file2.txt", "empty.txt", "file1.txt", "out.txt"}
        self.assertEqual(set(result), expected)

    def test_ls_no_args(self, out=deque()):
        eval("cd test/test_files", out)
        eval("ls", out)
        result = get_result(out, "\t")
        eval("cd /comp0010", out)
        result = set(result)
        self.assertEqual(
            result,
            {
                "dir1",
                "file2.txt",
                "empty.txt",
                "file1.txt",
                "out.txt"
            }
        )

    def test_ls_too_many_args(self, out=deque()):
        with self.assertRaises(FlagError):
            eval("ls test test/test_files", out)
