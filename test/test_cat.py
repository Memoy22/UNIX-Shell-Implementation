import unittest
from collections import deque
from parameterized import parameterized
from exceptions import (FlagError, StandardInputError)
from shell import eval
from utils.file import File


def get_result(out, split_type="\n"):
    result = []
    while out:
        result.append(out.popleft())
    return "".join(result).strip().split(split_type)


class TestCat(unittest.TestCase):
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
            # No files
            ([], [""]),
            # Single file
            ([file1], file1_content),
            # Multiple file
            ([file1, file2], file1_content + file2_content),
            # Empty file
            ([empty], empty_content),
        ]
    )
    def test_cat(self, file_paths, expected_result, out=deque()):
        eval(f"cat {' '.join(file_paths)}", out)
        result = get_result(out)
        self.assertEqual(result, expected_result)

    def test_cat_no_file_exists(self, out=deque()):
        with self.assertRaises(FlagError):
            eval("cat non_existing_file.txt", out)

    def test_cat_out_redir(self, out=deque()):
        eval(f"cat {self.file1} > {self.out_dir}", out)
        result = File.read(self.out_dir).strip().split("\n")
        self.assertEqual(result, self.file1_content)

    @parameterized.expand(
        [
            # Single file - file1
            (file1, file1_content),
            # Single file - file2
            (file2, file2_content),
            # Empty file
            (empty, empty_content),
        ]
    )
    def test_cat_in_redir(self, file_paths, expected_result, out=deque()):
        eval(f"cat < {file_paths}", out)
        result = get_result(out)
        self.assertEqual(result, expected_result)

    def test_cat_pipe(self, out=deque()):
        eval(f"echo {self.test_files_dir}/*.txt | cat", out)
        print('out:', out)
        result = get_result(out, " ")
        print('result:', result)
        result = set(result)
        print('set_result:', result)
        self.assertEqual(
            result,
            {
                "test/test_files/file2.txt",
                "test/test_files/empty.txt",
                "test/test_files/file1.txt",
                "test/test_files/out.txt"
            },
        )

    def test_multi_redir_in(self, out=deque()):
        with self.assertRaises(StandardInputError):
            eval(f"cat < {self.file1} < {self.file2}", out)

    def test_multi_redir_out(self, out=deque()):
        with self.assertRaises(StandardInputError):
            eval(
                f"cat {self.empty} > {self.file1} > {self.file2}", out
            )

    # def test_multi_redir_out_unsafe(self, out=deque()):
    #     eval(f"_cat {self.empty} > {self.file1} > {self.file2}", out)
    #     result = get_result(out)
    #     msg = "Error: Multiple redirections given"
    #     self.assertEqual(result, [msg])

    def test_multi_redir_in_out(self, out=deque()):
        with self.assertRaises(StandardInputError):
            eval(
                f"cat {self.file1}"
                f"< {self.file1} < {self.file2}"
                f"> {self.file1} > {self.file1}",
                out
            )

    def test_cat_sub(self, out=deque()):
        eval(f"cat `echo {self.file1}`", out)
        result = get_result(out)
        self.assertEqual(result, self.file1_content)

    def test_unsafe(self, out=deque()):
        file = "non_existing_file.txt"
        eval(f"_cat {file}", out=out)
        result = get_result(out)
        expected = [f"Error: '{file}': No such file or directory"]
        self.assertEqual(result, expected)

    def test_cat_redir_infront(self, out=deque()):
        eval(f"< {self.file1} cat", out)
        result = get_result(out)
        self.assertEqual(result, self.file1_content)

    def test_pipe_cat_head(self, out=deque()):
        eval(f"cat {self.file1} | head -n 2", out)
        result = get_result(out)
        self.assertEqual(result, self.file1_content[:2])

    def test_pipe_cat_tail(self, out=deque()):
        eval(f"cat {self.file1} | tail -n 2", out)
        result = get_result(out)
        self.assertEqual(result, self.file1_content[-2:])
