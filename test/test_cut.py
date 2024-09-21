import unittest
from collections import deque
from parameterized import parameterized
from exceptions import (FlagError, FlagValueError)
from shell import eval
from utils.file import File


def get_result(out, split_type="\n"):
    result = []
    while out:
        result.append(out.popleft())
    return "".join(result).strip().split(split_type)


class TestCut(unittest.TestCase):
    test_files_dir = "test/test_files"

    file1 = "test/test_files/file1.txt"
    file2 = "test/test_files/file2.txt"
    empty = "test/test_files/empty.txt"

    file1_content = ["Lorem", "Ipsum", "Dolor"]
    file2_content = ["ABCD", "EFGH", "IJKL", "MNOP"]
    empty_content = [""]

    @parameterized.expand(
        [
            # Empty file
            ("1,3,5", empty, [""]),
            # Individual bytes bigger than file line length - file1
            ("1,3,5,7", file1, ["Lrm", "Ism", "Dlr"]),
            # Individual bytes in random order - file 1
            ("5,2,7,3", file1, ["orm", "psm", "olr"]),
            # Closed ranges - file 1
            ("2-4", file1, ["ore", "psu", "olo"]),
            # Closed ranges bigger than file line length - file 1
            ("2-100", file1, ["orem", "psum", "olor"]),
            # Open ranges - file 1
            ("-2,4-", file1, ["Loem", "Ipum", "Door"]),
            # Overlapping closed ranges - file 1
            ("2-4,3-5", file1, ["orem", "psum", "olor"]),
            # Overlapping open ranges - file 1
            ("-3,2-", file1, ["Lorem", "Ipsum", "Dolor"]),
        ]
    )
    def test_cut(self, cut_options, file, expected_result, out=deque()):
        eval(f"cut -b {cut_options} {file}", out)
        result = get_result(out)
        self.assertEqual(result, expected_result)

    def test_cut_no_file_exists(self, out=deque()):
        with self.assertRaises(FlagError):
            eval("cut noExistsDirectory/file.txt", out)

    def test_cut_pipe(self, out=deque()):
        eval(f"cat {self.file1} | cut -b 2-4,3-5", out)
        result = get_result(out)
        self.assertEqual(result, ["orem", "psum", "olor"])

    def test_cut_sub(self, out=deque()):
        eval(f"cut -b 2-4,3-5 `echo {self.file1}`", out)
        result = get_result(out)
        self.assertEqual(result, ["orem", "psum", "olor"])

    def test_cut_redir_in(self, out=deque()):
        eval(f"cut -b 2-4,3-5 < {self.file1}", out)
        result = get_result(out)
        self.assertEqual(result, ["orem", "psum", "olor"])

    def test_cut_redir_out(self, out=deque()):
        eval(f"cut -b 2-4,3-5 {self.file1} > out.txt", out)
        result = File.read("out.txt").strip().split("\n")
        self.assertEqual(result, ["orem", "psum", "olor"])

    def test_cut_unsafe(self, out=deque()):
        file = "nonExistsFile.txt"
        eval(f"_cut -b 2-4,3-5 {file}", out=out)
        result = get_result(out)
        expected = [f"Error: '{file}': No such file or directory"]
        self.assertEqual(result, expected)

    def test_cut_wrong_args_type(self, out=deque()):
        with self.assertRaises(FlagError):
            eval(f"cut -b -c 1- {self.file1}", out)

    def test_cut_wrong_range(self, out=deque()):
        with self.assertRaises(FlagValueError):
            eval(f"cut -b 1-2-3 {self.file1}", out)

    def test_cut_invalid_byte(self, out=deque()):
        with self.assertRaises(FlagValueError):
            eval(f"cut -b a,3 {self.file1}", out)
