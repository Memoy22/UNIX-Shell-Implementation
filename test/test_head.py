import unittest
from collections import deque
from parameterized import parameterized
from exceptions import FlagError, FlagValueError
from shell import eval
from src.utils.file import File


def get_result(out, split_type="\n"):
    result = []
    while out:
        result.append(out.popleft())
    return "".join(result).strip().split(split_type)


class TestHead(unittest.TestCase):
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
            (2, empty, [""]),
            # n > len(lines) in file
            (30, file1, file1_content),
            # n == len(lines) in file
            (4, file2, file2_content),
            # n < len(lines) in file
            (2, file1, file1_content[:2]),
            # n == 0
            (0, file1, [""]),
        ]
    )
    def test_head(self, n, file, expected_result, out=deque()):
        eval(f"head -n {n} {file}", out)
        result = get_result(out)
        self.assertEqual(result, expected_result)

    def test_head_file_does_not_exist(self, out=deque()):
        with self.assertRaises(FlagError):
            eval("head File.txt", out)

    def test_head_no_args(self, out=deque()):
        with self.assertRaises(FlagError):
            eval("head", out)

    def test_head_negative_n(self, out=deque()):
        with self.assertRaises(FlagValueError):
            eval(f"head -n -3 {self.file1}", out)

    def test_head_pipe(self, out=deque()):
        eval("find test/test_files -name '*.txt' | head -n 3", out)
        result = get_result(out, "\n")
        result = set(result)
        self.assertEqual(
            result,
            {
                "test/test_files/file2.txt",
                "test/test_files/empty.txt",
                "test/test_files/file1.txt",
            },
        )

    def test_head_wrong_flag(self, out=deque()):
        with self.assertRaises(FlagError):
            eval(f"head -k 1 {self.file1}", out)

    def test_head_stdIn(self, out=deque()):
        eval(f"head < {self.file1}", out)
        result = get_result(out)
        self.assertEqual(result, self.file1_content)

    def test_head_default_n(self, out=deque()):
        eval(f"head {self.file1}", out)
        result = get_result(out)
        self.assertEqual(result, self.file1_content)

    def test_head_unsafe_stdIn(self, out=deque()):
        eval(f"_head < {self.file1}", out)
        result = get_result(out)
        self.assertEqual(result, self.file1_content)

    def test_head_unsafe_stdIn_not_exists(self, out=deque()):
        eval("_head < wrongFile.txt", out)
        result = get_result(out)
        msg = "Error: 'wrongFile.txt': No such file or directory"
        self.assertEqual(result, [msg])

    def test_head_redir_both(self, out=deque()):
        eval(f"head -n 2 < {self.file1} > out.txt", out)
        result = File.read("out.txt").strip().split("\n")
        self.assertEqual(result, self.file1_content[:2])

    def test_redir_in_front_unsafe(self, out=deque()):
        eval(f"< {self.file1} _head", out)
        result = get_result(out)
        self.assertEqual(result, self.file1_content)
