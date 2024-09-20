import unittest
from collections import deque
from parameterized import parameterized
from exceptions import FlagError
from shell import eval


def get_result(out, split_type="\n"):
    result = []
    while out:
        result.append(out.popleft())
    return "".join(result).strip().split(split_type)


class TestSort(unittest.TestCase):
    test_files_dir = "test/test_files"

    file1 = "test/test_files/file1.txt"
    file2 = "test/test_files/file2.txt"
    empty = "test/test_files/empty.txt"

    file1_content = ["Lorem", "Ipsum", "Dolor"]
    file2_content = ["ABCD", "EFGH", "IJKL", "MNOP"]
    empty_content = [""]

    @parameterized.expand(
        [
            # Empty File
            ("", empty, [""]),
            # File with multiple lines-take numeric sorting into consideration
            (
                    "",
                    "test/test_files/dir1/dir1_subdir1/find.txt",
                    ["4hello", "m1emoy", "me1moy", "memoy"],
            ),
            # File with multiple lines in reverse
            (
                    "-r",
                    "test/test_files/dir1/dir1_subdir1/find.txt",
                    ["4hello", "m1emoy", "me1moy", "memoy"][::-1],
            ),
            # File that is already sorted
            ("", file2, file2_content),
            # File with single character
            ("", "test/test_files/dir1/dir1_subdir1/find2.txt", ["H"]),
            # File with single character in reverse
            ("-r", "test/test_files/dir1/dir1_subdir1/find2.txt", ["H"]),
        ]
    )
    def test_sort(self, rev, file, expected_result, out=deque()):
        eval(f"sort {rev} {file}", out)
        result = get_result(out)
        self.assertEqual(result, expected_result)

    def test_sort_file_not_exists(self, out=deque()):
        with self.assertRaises(FlagError):
            eval("sort wrongFile.txt", out)

    def test_sort_no_args(self, out=deque()):
        with self.assertRaises(FlagError):
            eval("sort", out)
