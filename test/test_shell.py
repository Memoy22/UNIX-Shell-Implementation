import io
import os
import unittest
from unittest.mock import patch

from collections import deque

from parameterized import parameterized

from exceptions import (FlagError, InvalidFormatError,
                        MultipleRedirectionError, FileAlreadyExistsError, CommandNotFoundError)
from shell import eval, interactive_mode, main
from utils import File


def get_result(out, split_type="\n"):
    result = []
    while out:
        result.append(out.popleft())
    return "".join(result).strip().split(split_type)


class TestShell(unittest.TestCase):
    test_files_dir = "test/test_files"

    file1 = "test/test_files/file1.txt"
    file2 = "test/test_files/file2.txt"
    empty = "test/test_files/empty.txt"

    file1_content = ["Lorem", "Ipsum", "Dolor"]
    file2_content = ["ABCD", "EFGH", "IJKL", "MNOP"]
    empty_content = [""]

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
        eval(f"cat {self.file1} > out.txt", out)
        result = File("out.txt").read().strip().split("\n")
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
            },
        )

    def test_multi_redir_in(self, out=deque()):
        with self.assertRaises(MultipleRedirectionError):
            eval(f"cat < {self.file1} < {self.file2}", out)

    def test_multi_redir_out(self, out=deque()):
        with self.assertRaises(MultipleRedirectionError):
            eval(f"cat {self.empty} > {self.file1} > {self.file2}", out)

    # def test_multi_redir_out_unsafe(self, out=deque()):
    #     eval(f"_cat {self.empty} > {self.file1} > {self.file2}", out)
    #     result = get_result(out)
    #     msg = "Error: Multiple redirections given"
    #     self.assertEqual(result, [msg])

    def test_empty_cmdline(self, out=deque()):
        eval("", out)
        result = get_result(out)
        self.assertEqual(result, [""])

    def test_multi_redir_in_out(self, out=deque()):
        with self.assertRaises(MultipleRedirectionError):
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

    def test_cd_change_dir(self, out=deque()):
        eval(f"cd {self.test_files_dir}; echo *.txt", out)
        eval("cd /comp0010", out)  # To come to comp0010 directory for other tests
        result = get_result(out, " ")
        result = set(result)
        self.assertEqual(result, {"file2.txt", "empty.txt", "file1.txt"})

    def test_cd_change_dir_relative(self, out=deque()):
        eval(f"cd {self.test_files_dir}; cd ..; echo *.py", out)
        eval("cd /comp0010", out)  # To come to comp0010 directory for other tests
        result = get_result(out, " ")
        self.assertEqual(result, ["test_shell.py"])

    def test_cd_non_existing_dir(self, out=deque()):
        with self.assertRaises(FlagError):
            eval("cd nonExistingDirectory/", out)

    def test_echo_quotes_inside_args(self, out=deque()):
        eval('echo a"b"c', out)
        result = get_result(out)
        self.assertEqual(result, ["abc"])

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
        result = File("out.txt").read().strip().split("\n")
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
        with self.assertRaises(InvalidFormatError):
            eval(f"cut -b 1-2-3 {self.file1}", out)

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
        eval("echo foo bar > out.txt", out)
        result = File("out.txt").read().strip().split("\n")
        self.assertEqual(result, ["foo bar"])

    def test_echo_redir_in_file_not_exists(self, out=deque()):
        with self.assertRaises(FlagError):
            eval("echo < abcd.txt", out)

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
    def test_find_directory_given(self, directory, file, expected_result, out=deque()):
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
    def test_find_directory_not_given(self, file, expected_result, out=deque()):
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
        eval("find -name 'find.txt' > out.txt", out)
        result = File("out.txt").read().strip().split("\n")
        expected = ["./test/test_files/dir1/dir1_subdir1/find.txt"]
        self.assertEqual(result, expected)

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
        eval(f"grep [a-z] {self.file1} > out.txt", out)
        result = File("out.txt").read().strip().split("\n")
        self.assertEqual(result, self.file1_content)

    def test_grep_redir_in(self, out=deque()):
        eval(f"grep [a-z] < {self.file1}", out)
        result = get_result(out)
        self.assertEqual(result, self.file1_content)

    def test_grep_file_not_exists_1(self, out=deque()):
        with self.assertRaises(FlagError):
            eval("grep A... file5.txt", out)

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
        with self.assertRaises(InvalidFormatError):
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

    @parameterized.expand(
        [
            # Directory containing file and folders
            ("test/test_files", ["dir1", "file2.txt", "empty.txt", "file1.txt"]),
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
        eval("ls test/test_files > out.txt", out)
        result = File("out.txt").read().strip().split("\t")
        expected = ["dir1", "file2.txt", "empty.txt", "file1.txt"]
        self.assertEqual(set(result), set(expected))

    def test_pwd(self, out=deque()):
        eval("pwd", out)
        result = get_result(out)
        self.assertEqual(result, os.getcwd().strip().split("\n"))

    def test_pwd_redir_out(self, out=deque()):
        eval("pwd > out.txt", out)
        result = File("out.txt").read().strip().split("\n")
        self.assertEqual(result, os.getcwd().strip().split("\n"))

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

    @parameterized.expand(
        [
            # Empty File
            ("", empty, [""]),
            # File with multiple lines - takes numeric sorting into
            # consideration
            (
                "",
                "test/test_files/dir1/dir1_subdir3/forUniq.txt",
                ["Apple", "apple", "banana", "apple", "banana", "banAna", "Orange"],
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
                ["Apple", "apple", "banana", "apple", "banana", "banAna", "Orange"],
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
    def test_uniq_stdIn(self, case_insensitive, file, expected_result, out=deque()):
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

    def test_redir_both(self, out=deque()):
        eval(f"head -n 2 < {self.file1} > out.txt", out)
        result = File("out.txt").read().strip().split("\n")
        self.assertEqual(result, self.file1_content[:2])

    def test_redir_infront_cat(self, out=deque()):
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

    def test_pipe_echo_cut(self, out=deque()):
        eval("echo abc | cut -b 1", out)
        result = get_result(out)
        self.assertEqual(result, ["a"])

    def test_unsafe_command_not_exists(self, out=deque()):
        with self.assertRaises(CommandNotFoundError):
            eval("_wrong", out)

    def test_cd_no_args(self, out=deque()):
        eval("cd; pwd", out)
        result = get_result(out)
        self.assertEqual(result, [os.getcwd()])

    def test_cut_invalid_byte(self, out=deque()):
        with self.assertRaises(InvalidFormatError):
            eval(f"cut -b a,3 {self.file1}", out)

    def test_find_too_many_args(self, out=deque()):
        with self.assertRaises(FlagError):
            eval(f"find {self.test_files_dir} -name -hello -hi 'file.txt'", out)

    def test_grep_too_many_args(self, out=deque()):
        with self.assertRaises(FlagError):
            eval(f"grep A... B... {self.file1} {self.file2}", out)

    def test_head_stdIn(self, out=deque()):
        eval(f"head < {self.file1}", out)
        result = get_result(out)
        self.assertEqual(result, self.file1_content)

    def test_head_default_n(self, out=deque()):
        eval(f"head {self.file1}", out)
        result = get_result(out)
        self.assertEqual(result, self.file1_content)

    def test_ls_no_args(self, out=deque()):
        eval("cd test/test_files", out)
        eval("ls", out)
        result = get_result(out, "\t")
        eval("cd /comp0010", out)
        result = set(result)
        self.assertEqual(result, {"dir1", "file2.txt", "empty.txt", "file1.txt"})

    def test_ls_too_many_args(self, out=deque()):
        with self.assertRaises(FlagError):
            eval("ls test test/test_files", out)

    def test_grep_no_args(self, out=deque()):
        with self.assertRaises(FlagError):
            eval("grep", out)

    def test_tail_stdIn(self, out=deque()):
        eval(f"tail < {self.file1}", out)
        result = get_result(out)
        self.assertEqual(result, self.file1_content)

    def test_tail_default_n(self, out=deque()):
        eval(f"tail {self.file1}", out)
        result = get_result(out)
        self.assertEqual(result, self.file1_content)

    def test_tail_too_many_args(self, out=deque()):
        with self.assertRaises(FlagError):
            eval(f"tail -n -j 3 {self.file1}", out)

    def test_head_unsafe_stdIn(self, out=deque()):
        eval(f"_head < {self.file1}", out)
        result = get_result(out)
        self.assertEqual(result, self.file1_content)

    def test_head_unsafe_stdIn_not_exists(self, out=deque()):
        eval("_head < wrongFile.txt", out)
        result = get_result(out)
        msg = "Error: 'wrongFile.txt': No such file or directory"
        self.assertEqual(result, [msg])

    def test_echo_sub(self, out=deque()):
        eval("echo a`echo a`a", out)
        result = get_result(out)
        self.assertEqual(result, ["aaa"])

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

    def test_mkdir(self, out=deque()):
        eval("mkdir mkdir_test; ls", out)
        result = get_result(out, "\t")
        self.assertTrue("mkdir_test" in result)

    def test_mkdir_multiple(self, out=deque()):
        eval("mkdir -p mkdir_test1 mkdir_test2; ls", out)
        result = get_result(out, "\t")
        self.assertTrue({'mkdir_test1', 'mkdir_test2'}.issubset(result))

    def test_mkdir_already_exists(self, out=deque()):
        with self.assertRaises(FileAlreadyExistsError):
            eval("mkdir test", out)

    def test_mkdir_missing_operand(self, out=deque()):
        with self.assertRaises(FlagError):
            eval("mkdir", out)

    def test_mkdir_p(self, out=deque()):
        with self.assertRaises(FlagError):
            eval("mkdir -p", out)

    def test_mkdir_missing_p(self, out=deque()):
        with self.assertRaises(FlagError):
            eval("mkdir a/b", out)

    def test_redir_in_front_unsafe(self, out=deque()):
        eval(f"< {self.file1} _head", out)
        result = get_result(out)
        self.assertEqual(result, self.file1_content)

    def test_shell_main(self, out=deque()):
        with patch("sys.argv", new=["script_name", "-c", "echo"]):
            with patch("sys.stdout", new_callable=io.StringIO) as mstdO:
                main()
                self.assertEqual(mstdO.getvalue().strip(), "")

    def test_shell_main_ValueError_0(self, out=deque()):
        with patch("sys.argv", new=["script_name", "echo foo bar", "-c"]):
            with patch("sys.stdout", new_callable=io.StringIO):
                with self.assertRaises(ValueError):
                    main()

    def test_shell_main_ValueError_1(self, out=deque()):
        with patch("sys.argv", new=["script_name", "-c", "echo foo", "echo ss"]):
            with patch("sys.stdout", new_callable=io.StringIO):
                with self.assertRaises(ValueError):
                    main()

    @patch("builtins.input", return_value="echo")
    @patch("builtins.print")
    def test_interactive_mode(self, mock_input, mock_print, out=deque()):
        with io.StringIO() as buf, patch("sys.stdout", buf):
            interactive_mode()
            output = buf.getvalue()
        expected_output = ""
        self.assertIn(expected_output, output)


if __name__ == "__main__":
    unittest.main()
