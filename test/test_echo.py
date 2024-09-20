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


class TestEcho(unittest.TestCase):
    test_files_dir = "test/test_files"

    file1 = "test/test_files/file1.txt"
    file2 = "test/test_files/file2.txt"
    empty = "test/test_files/empty.txt"

    file1_content = ["Lorem", "Ipsum", "Dolor"]
    file2_content = ["ABCD", "EFGH", "IJKL", "MNOP"]
    empty_content = [""]

    out_dir = "test/test_files/out.txt"

    def test_echo_quotes_inside_args(self, out=deque()):
        eval('echo a"b"c', out)
        result = get_result(out)
        self.assertEqual(result, ["abc"])

    @parameterized.expand(
        [
            # Single arg
            (["foo"], ["foo"]),
            # Multiple arg
            (["foo", "bar"], ["foo", "bar"]),
            # Globbing
            (
                    [f"{test_files_dir}/*.txt"],
                    [
                        "test/test_files/file2.txt",
                        "test/test_files/empty.txt",
                        "test/test_files/file1.txt",
                    ],
            ),
            # No argument
            ([""], [""]),
            # Double Quotes
            (["foo bar"], ["foo", "bar"]),
            # Single Quotes
            (["foo bar"], ["foo", "bar"]),
            # SQ containing substitution - No substitution should occur
            (["'foo `echo bar`'"], ["foo", "`echo", "bar`"]),
            # Substitution inside DQ
            (['foo "`echo bar`"'], ["foo", "bar"]),
            # Substitution in second arg
            (["foo `echo bar`"], ["foo", "bar"]),
            # Piping - Echo should not read from stdIn
            (["foo | echo"], [""]),
            # Input Redirection - Echo should not read from stdIn
            ([f"foo < {file1}"], ["foo"]),
            # Input Redirection - Echo should not read from stdIn
            ([f"< {file1}"], [""]),
        ]
    )
    def test_echo(self, args, expected_result, out=deque()):
        eval(f"echo {' '.join(args)}", out)
        result = get_result(out, " ")
        result = set(result)
        self.assertEqual(result, set(expected_result))

    def test_echo_whitespace(self, out=deque()):
        eval("echo 'a   b'", out)
        result = get_result(out)
        self.assertEqual(result, ["a   b"])

    def test_echo_cmd_sub(self, out=deque()):
        eval(f"`echo head` -n 2 {self.file1}", out)
        result = get_result(out)
        self.assertEqual(result, self.file1_content[:2])

    def test_echo_redir_out(self, out=deque()):
        eval(f"echo foo bar > {self.out_dir}", out)
        result = File(self.out_dir).read().strip().split("\n")
        self.assertEqual(result, ["foo bar"])

    def test_echo_redir_in_file_not_exists(self, out=deque()):
        with self.assertRaises(FlagError):
            eval("echo < abcd.txt", out)

    def test_echo_sub(self, out=deque()):
        eval("echo a`echo a`a", out)
        result = get_result(out)
        self.assertEqual(result, ["aaa"])

    def test_pipe_echo_cut(self, out=deque()):
        eval("echo abc | cut -b 1", out)
        result = get_result(out)
        self.assertEqual(result, ["a"])
