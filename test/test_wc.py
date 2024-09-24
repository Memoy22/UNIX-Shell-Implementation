import unittest
from collections import deque
from exceptions import FlagError
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

    def test_wc(self, out=deque()):
        eval(f"wc {self.file1}", out)
        result = get_result(out)
        self.assertEqual(result, ['3 3 18'])

    def test_wc_l(self, out=deque()):
        eval(f"wc -l {self.file2}", out)
        result = get_result(out)
        self.assertEqual(result, ['4'])

    def test_wc_w(self, out=deque()):
        eval(f"wc -w {self.file2}", out)
        result = get_result(out)
        self.assertEqual(result, ['4'])

    def test_wc_m(self, out=deque()):
        eval(f"wc -m {self.file1} {self.file2}", out)
        result = get_result(out)
        self.assertEqual(result, ['37'])

    def test_wc_wrong_flag(self, out=deque()):
        with self.assertRaises(FlagError):
            eval(f"wc -f {self.file1} {self.file2}", out)

    def test_wc_no_arg(self, out=deque()):
        with self.assertRaises(FlagError):
            eval("wc", out)

    def test_wc_stdin(self, out=deque()):
        eval(f"wc -l < {self.file1}", out)
        result = get_result(out)
        self.assertEqual(result, ['3'])

    def test_wc_no_arg_stdin(self, out=deque()):
        eval(f"wc < {self.file1}", out)
        result = get_result(out)
        self.assertEqual(result, ['3 3 18'])
