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


class TestUniq(unittest.TestCase):
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
            # File with multiple lines - takes numeric sorting into
            # consideration
            (
                    "",
                    "test/test_files/dir1/dir1_subdir3/forUniq.txt",
                    [
                        "Apple",
                        "apple",
                        "banana",
                        "apple",
                        "banana",
                        "banAna",
                        "Orange"
                    ],
            ),
            # File with multiple lines with -i flag
            (
                    "-i",
                    "test/test_files/dir1/dir1_subdir3/forUniq.txt",
                    ["Apple", "banana", "apple", "banana", "Orange"],
            ),
            # File that is already uniq
            ("", file2, file2_content),
            # File with single character
            ("", "test/test_files/dir1/dir1_subdir1/find2.txt", ["H"]),
            # File with single character in reverse
            ("-i", "test/test_files/dir1/dir1_subdir1/find2.txt", ["H"]),
        ]
    )
    def test_uniq(self, case_insensitive, file, expected_result, out=deque()):
        eval(f"uniq {case_insensitive} {file}", out)
        result = get_result(out)
        self.assertEqual(result, expected_result)

    @parameterized.expand(
        [
            # Empty File
            ("", empty, [""]),
            # File with multiple lines - takes numeric sorting into
            # consideration
            (
                    "",
                    "test/test_files/dir1/dir1_subdir3/forUniq.txt",
                    [
                        "Apple",
                        "apple",
                        "banana",
                        "apple",
                        "banana",
                        "banAna",
                        "Orange"
                    ],
            ),
            # File with multiple lines with -i flag
            (
                    "-i",
                    "test/test_files/dir1/dir1_subdir3/forUniq.txt",
                    ["Apple", "banana", "apple", "banana", "Orange"],
            ),
            # File that is already uniq
            ("", file2, file2_content),
            # File with single character
            ("", "test/test_files/dir1/dir1_subdir1/find2.txt", ["H"]),
            # File with single character in reverse
            ("-i", "test/test_files/dir1/dir1_subdir1/find2.txt", ["H"]),
        ]
    )
    def test_uniq_stdIn(self, case_insensitive, file, expected_result,
                        out=deque()):
        eval(f"uniq {case_insensitive} < {file}", out)
        result = get_result(out)
        self.assertEqual(result, expected_result)

    def test_uniq_file_not_exists(self, out=deque()):
        with self.assertRaises(FlagError):
            eval("uniq wrongFile.txt", out)

    def test_uniq_no_args(self, out=deque()):
        with self.assertRaises(FlagError):
            eval("uniq", out)

    def test_uniq_wrong_flag(self, out=deque()):
        with self.assertRaises(FlagError):
            eval(f"uniq -f {self.file1}", out)
