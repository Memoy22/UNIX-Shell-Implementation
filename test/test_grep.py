import unittest
from collections import deque
from parameterized import parameterized
from exceptions import FlagError
from shell import eval
from src.utils.file import File


def get_result(out, split_type="\n"):
    result = []
    while out:
        result.append(out.popleft())
    return "".join(result).strip().split(split_type)


class TestGrep(unittest.TestCase):
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
            # Empty File
            ("[a-z]", [empty], [""]),
            # Pattern not present
            ("1...", [file1], [""]),
            # Multiple input file
            (
                    "[A-Z]",
                    [file1, file2],
                    [
                        "test/test_files/file1.txt:Lorem",
                        "test/test_files/file1.txt:Ipsum",
                        "test/test_files/file1.txt:Dolor",
                        "test/test_files/file2.txt:ABCD",
                        "test/test_files/file2.txt:EFGH",
                        "test/test_files/file2.txt:IJKL",
                        "test/test_files/file2.txt:MNOP",
                    ],
            ),
        ]
    )
    def test_grep(self, pattern, files, expected_result, out=deque()):
        eval(f"grep {pattern} {' '.join(files)}", out)
        result = get_result(out)
        self.assertEqual(result, expected_result)

    def test_grep_pattern_sub(self, out=deque()):
        eval(f"grep `echo [a-z]` {self.file1}", out)
        result = get_result(out)
        self.assertEqual(result, self.file1_content)

    def test_grep_file_not_exists_0(self, out=deque()):
        with self.assertRaises(FlagError):
            eval("grep A... test/test_files/file3.txt", out)

    def test_grep_redir_out(self, out=deque()):
        eval(f"grep [a-z] {self.file1} > {self.out_dir}", out)
        result = File.read(self.out_dir).strip().split("\n")
        self.assertEqual(result, self.file1_content)

    def test_grep_redir_in(self, out=deque()):
        eval(f"grep [a-z] < {self.file1}", out)
        result = get_result(out)
        self.assertEqual(result, self.file1_content)

    def test_grep_file_not_exists_1(self, out=deque()):
        with self.assertRaises(FlagError):
            eval("grep A... file5.txt", out)

    def test_grep_too_many_args(self, out=deque()):
        with self.assertRaises(FlagError):
            eval(f"grep A... B... {self.file1} {self.file2}", out)

    def test_grep_no_args(self, out=deque()):
        with self.assertRaises(FlagError):
            eval("grep", out)
