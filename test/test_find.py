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


class TestFind(unittest.TestCase):
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
            # Directory provided - globbing pattern in file name
            (
                    "test/test_files/dir1",
                    "*.txt",
                    [
                        "test/test_files/dir1/dir1_subdir3/forUniq.txt",
                        "test/test_files/dir1/dir1_subdir3/alreadyUniq.txt",
                        "test/test_files/dir1/dir1_subdir1/find2.txt",
                        "test/test_files/dir1/dir1_subdir1/find.txt",
                    ],
            ),
            # Directory provided - no globbing in file name
            (
                    "test/test_files/dir1",
                    "find.txt",
                    ["test/test_files/dir1/dir1_subdir1/find.txt"],
            ),
            # Directory provided - file does not exist
            ("test/test_files/dir1", "doesNotExist.txt", [""]),
            # Directory provided - filename in quotes
            (
                    "test/test_files/dir1",
                    "'find.txt'",
                    ["test/test_files/dir1/dir1_subdir1/find.txt"],
            ),
        ]
    )
    def test_find_directory_given(self, directory, file, expected_result,
                                  out=deque()):
        eval(f"find {directory} -name {file}", out)
        result = get_result(out)
        result = set(result)
        self.assertEqual(result, set(expected_result))

    @parameterized.expand(
        [
            # Globbing pattern in file name
            ("*.csv", ["./test/test_files/dir1/dir1_subdir2/file.csv"]),
            # File name provided
            ("find.txt", ["./test/test_files/dir1/dir1_subdir1/find.txt"]),
            # File does not exist
            ("find5.txt", [""]),
        ]
    )
    def test_find_directory_not_given(self, file, expected_result,
                                      out=deque()):
        eval(f"find -name {file}", out)
        result = get_result(out)
        self.assertEqual(result, expected_result)

    def test_find_directory_not_exists(self, out=deque()):
        with self.assertRaises(FlagError):
            eval("find wrongDir -name '*.txt'", out)

    def test_find_wrong_flag(self, out=deque()):
        with self.assertRaises(FlagError):
            eval("find test_files -names '*.txt'", out)

    def test_find_redir_out(self, out=deque()):
        eval(f"find -name 'find.txt' > {self.out_dir}", out)
        result = File.read(self.out_dir).strip().split("\n")
        expected = ["./test/test_files/dir1/dir1_subdir1/find.txt"]
        self.assertEqual(result, expected)

    def test_find_too_many_args(self, out=deque()):
        with self.assertRaises(FlagError):
            eval(
        f"find {self.test_files_dir} -name -hello -hi 'file.txt'",
                out
            )
