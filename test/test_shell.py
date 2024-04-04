import io
import os
import unittest
from unittest.mock import patch

from parameterized import parameterized

from exceptions import (FlagError, InvalidFormatError,
                        MultipleRedirectionError, FileAlreadyExistsError)
from shell import eval, interactive_mode, main
from utility import File


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
    def test_cat(self, file_paths, expected_result):
        out = eval(f"cat {' '.join(file_paths)}")
        result = out.popleft().strip().split("\n")
        self.assertEqual(result, expected_result)

    def test_cat_no_file_exists(self):
        with self.assertRaises(FlagError):
            eval("cat non_existing_file.txt")

    def test_cat_out_redir(self):
        eval(f"cat {self.file1} > out.txt")
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
    def test_cat_in_redir(self, file_paths, expected_result):
        out = eval(f"cat < {file_paths}")
        result = out.popleft().strip().split("\n")
        self.assertEqual(result, expected_result)

    def test_cat_pipe(self):
        out = eval(f"echo {self.test_files_dir}/*.txt | cat")
        result = out.popleft().strip().split(" ")
        result = set(result)
        self.assertEqual(
            result,
            {
                "test/test_files/file2.txt",
                "test/test_files/empty.txt",
                "test/test_files/file1.txt",
            },
        )

    def test_multi_redir_in(self):
        with self.assertRaises(MultipleRedirectionError):
            eval(f"cat < {self.file1} {self.file2}")

    def test_multi_redir_out(self):
        with self.assertRaises(MultipleRedirectionError):
            eval(f"cat {self.empty} > {self.file1} {self.file2}")

    def test_multi_redir_out_unsafe(self):
        out = eval(f"_cat {self.empty} > {self.file1} {self.file2}")
        result = out.popleft().strip().split("\n")
        msg = "Error: Multiple Output Redirections given"
        self.assertEqual(result, [msg])

    def test_empty_cmdline(self):
        out = eval("")
        result = out.popleft().strip().split("\n")
        self.assertEqual(result, [""])

    def test_multi_redir_in_out(self):
        with self.assertRaises(MultipleRedirectionError):
            eval(
                f"cat {self.file1}"
                f"< {self.file1} {self.file2}"
                f"> {self.file1} {self.file1}"
            )

    def test_cat_sub(self):
        out = eval(f"cat `echo {self.file1}`")
        result = out.popleft().strip().split("\n")
        self.assertEqual(result, self.file1_content)

    def test_unsafe(self):
        file = "non_existing_file.txt"
        out = eval(f"_cat {file}")
        result = out.popleft().strip().split("\n")
        expected = [f"Error: '{file}': No such file or directory"]
        self.assertEqual(result, expected)

    def test_cd_change_dir(self):
        out = eval(f"cd {self.test_files_dir}; echo *.txt")
        eval("cd /comp0010")  # To come to comp0010 directory for other tests
        result = out.popleft().strip().split(" ")
        result = set(result)
        self.assertEqual(result, {"file2.txt", "empty.txt", "file1.txt"})

    def test_cd_change_dir_relative(self):
        out = eval(f"cd {self.test_files_dir}; cd ..; echo *.py")
        eval("cd /comp0010")  # To come to comp0010 directory for other tests
        result = out.popleft().strip().split(" ")
        self.assertEqual(result, ["test_shell.py"])

    def test_cd_non_existing_dir(self):
        with self.assertRaises(FlagError):
            eval("cd nonExistingDirectory/")

    def test_echo_quotes_inside_args(self):
        out = eval('echo a"b"c')
        result = out.popleft().strip().split("\n")
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
            # open ranges - file 1
            ("-2,4-", file1, ["Loem", "Ipum", "Door"]),
            # Overlapping closed ranges - file 1
            ("2-4,3-5", file1, ["orem", "psum", "olor"]),
            # Overlapping open ranges - file 1
            ("-3,2-", file1, ["Lorem", "Ipsum", "Dolor"]),
        ]
    )
    def test_cut(self, cut_options, file, expected_result):
        out = eval(f"cut -b {cut_options} {file}")
        result = out.popleft().strip().split("\n")
        self.assertEqual(result, expected_result)

    def test_cut_no_file_exists(self):
        with self.assertRaises(FlagError):
            eval("cut noExistsDirectory/file.txt")

    def test_cut_pipe(self):
        out = eval(f"cat {self.file1} | cut -b 2-4,3-5")
        result = out.popleft().strip().split("\n")
        self.assertEqual(result, ["orem", "psum", "olor"])

    def test_cut_sub(self):
        out = eval(f"cut -b 2-4,3-5 `echo {self.file1}`")
        result = out.popleft().strip().split("\n")
        self.assertEqual(result, ["orem", "psum", "olor"])

    def test_cut_redir_in(self):
        out = eval(f"cut -b 2-4,3-5 < {self.file1}")
        result = out.popleft().strip().split("\n")
        self.assertEqual(result, ["orem", "psum", "olor"])

    def test_cut_redir_out(self):
        eval(f"cut -b 2-4,3-5 {self.file1} > out.txt")
        result = File("out.txt").read().strip().split("\n")
        self.assertEqual(result, ["orem", "psum", "olor"])

    def test_cut_unsafe(self):
        file = "nonExistsFile.txt"
        out = eval(f"_cut -b 2-4,3-5 {file}")
        result = out.popleft().strip().split("\n")
        expected = [f"Error: '{file}': No such file or directory"]
        self.assertEqual(result, expected)

    def test_cut_wrong_args_type(self):
        with self.assertRaises(FlagError):
            eval(f"cut -b -c 1- {self.file1}")

    def test_cut_wrong_range(self):
        with self.assertRaises(InvalidFormatError):
            eval(f"cut -b 1-2-3 {self.file1}")

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
    def test_echo(self, args, expected_result):
        out = eval(f"echo {' '.join(args)}")
        result = out.popleft().strip().split(" ")
        result = set(result)
        self.assertEqual(result, set(expected_result))

    def test_echo_whitespace(self):
        out = eval("echo 'a   b'")
        result = out.popleft().strip()
        self.assertEqual(result, "a   b")

    def test_echo_cmd_sub(self):
        out = eval(f"`echo head` -n 2 {self.file1}")
        result = out.popleft().strip().split("\n")
        self.assertEqual(result, self.file1_content[:2])

    def test_echo_redir_out(self):
        eval("echo foo bar > out.txt")
        result = File("out.txt").read().strip().split(" ")
        self.assertEqual(result, ["foo", "bar"])

    def test_echo_redir_in_file_not_exists(self):
        with self.assertRaises(FlagError):
            eval("echo < abcd.txt")

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
    def test_find_directory_given(self, directory, file, expected_result):
        out = eval(f"find {directory} -name {file}")
        result = out.popleft().strip().split("\n")
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
    def test_find_directory_not_given(self, file, expected_result):
        out = eval(f"find -name {file}")
        result = out.popleft().strip().split("\n")
        self.assertEqual(result, expected_result)

    def test_find_directory_not_exists(self):
        with self.assertRaises(FlagError):
            eval("find wrongDir -name '*.txt'")

    def test_find_wrong_flag(self):
        with self.assertRaises(FlagError):
            eval("find test_files -names '*.txt'")

    def test_find_redir_out(self):
        eval("find -name 'find.txt' > out.txt")
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
    def test_grep(self, pattern, files, expected_result):
        out = eval(f"grep {pattern} {' '.join(files)}")
        result = out.popleft().strip().split("\n")
        self.assertEqual(result, expected_result)

    def test_grep_pattern_sub(self):
        out = eval(f"grep `echo [a-z]` {self.file1}")
        result = out.popleft().strip().split("\n")
        self.assertEqual(result, self.file1_content)

    def test_grep_file_not_exists_0(self):
        with self.assertRaises(FlagError):
            eval("grep A... test/test_files/file3.txt")

    def test_grep_redir_out(self):
        eval(f"grep [a-z] {self.file1} > out.txt")
        result = File("out.txt").read().strip().split("\n")
        self.assertEqual(result, self.file1_content)

    def test_grep_redir_in(self):
        out = eval(f"grep [a-z] < {self.file1}")
        result = out.popleft().strip().split("\n")
        self.assertEqual(result, self.file1_content)

    def test_grep_file_not_exists_1(self):
        with self.assertRaises(FlagError):
            eval("grep A... file5.txt")

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
    def test_head(self, n, file, expected_result):
        out = eval(f"head -n {n} {file}")
        result = out.popleft().strip().split("\n")
        self.assertEqual(result, expected_result)

    def test_head_file_does_not_exist(self):
        with self.assertRaises(FlagError):
            eval("head File.txt")

    def test_head_no_args(self):
        with self.assertRaises(FlagError):
            eval("head")

    def test_head_negative_n(self):
        with self.assertRaises(InvalidFormatError):
            eval(f"head -n -3 {self.file1}")

    def test_head_pipe(self):
        out = eval("find test/test_files -name '*.txt' | head -n 3")
        result = out.popleft().strip().split("\n")
        result = set(result)
        self.assertEqual(
            result,
            {
                "test/test_files/file2.txt",
                "test/test_files/empty.txt",
                "test/test_files/file1.txt",
            },
        )

    def test_head_wrong_flag(self):
        with self.assertRaises(FlagError):
            eval(f"head -k 1 {self.file1}")

    @parameterized.expand(
        [
            # Directory containing file and folders
            ("test/test_files", ["dir1", "file2.txt",
                                 "empty.txt", "file1.txt"]),
            # Directory containing file with name starting with '.'
            ("test/test_files/dir1/dir1_subdir2", ["file.csv"]),
        ]
    )
    def test_ls(self, directory, expected_result):
        out = eval(f"ls {directory}")
        result = out.popleft().strip().split("\t")
        result = set(result)
        self.assertEqual(result, set(expected_result))

    def test_ls_dir_not_exists(self):
        with self.assertRaises(FlagError):
            eval("ls notExistsDir")

    def test_ls_redir_in(self):
        eval("ls test/test_files > out.txt")
        result = File("out.txt").read().strip().split("\t")
        expected = ["dir1", "file2.txt", "empty.txt", "file1.txt"]
        self.assertEqual(set(result), set(expected))

    def test_pwd(self):
        out = eval("pwd")
        result = out.popleft().strip().split("\n")
        self.assertEqual(result, os.getcwd().strip().split("\n"))

    def test_pwd_redir_out(self):
        eval("pwd > out.txt")
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
    def test_sort(self, rev, file, expected_result):
        out = eval(f"sort {rev} {file}")
        result = out.popleft().strip().split("\n")
        self.assertEqual(result, expected_result)

    def test_sort_file_not_exists(self):
        with self.assertRaises(FlagError):
            eval("sort wrongFile.txt")

    def test_sort_no_args(self):
        with self.assertRaises(FlagError):
            eval("sort")

    @parameterized.expand(
        [
            # Empty File
            ("", empty, [""]),
            # Multiple lines file - takes numeric sorting into consideration
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
    def test_sort_stdIn(self, rev, file, expected_result):
        out = eval(f"sort {rev} < {file}")
        result = out.popleft().strip().split("\n")
        self.assertEqual(result, expected_result)

    def test_sort_wrong_flag(self):
        with self.assertRaises(FlagError):
            eval(f"sort -f {self.file1}")

    @parameterized.expand(
        [
            # Empty File
            (2, empty, [""]),
            # n > len(lines) in file
            (30, file1, file1_content),
            # n == len(lines) in file
            (4, file2, file2_content),
            # n < len(lines) in file
            (2, file1, file1_content[-2:]),
            # n == 0
            (0, file1, [""]),
        ]
    )
    def test_tail(self, n, file, expected_result):
        out = eval(f"tail -n {n} {file}")
        result = out.popleft().strip().split("\n")
        self.assertEqual(result, expected_result)

    def test_tail_file_does_not_exist(self):
        with self.assertRaises(FlagError):
            eval("head File.txt")

    def test_tail_no_args(self):
        with self.assertRaises(FlagError):
            eval("head")

    def test_tail_negative_n(self):
        with self.assertRaises(InvalidFormatError):
            eval(f"head -n -3 {self.file1}")

    def test_tail_pipe(self):
        out = eval("find test/test_files -name '*.txt' | tail -n 50")
        result = out.popleft().strip().split("\n")
        result = set(result)
        self.assertEqual(
            result,
            {
                "test/test_files/file2.txt",
                "test/test_files/empty.txt",
                "test/test_files/file1.txt",
                "test/test_files/dir1/dir1_subdir1/find2.txt",
                "test/test_files/dir1/dir1_subdir1/find.txt",
                "test/test_files/dir1/dir1_subdir3/forUniq.txt",
                "test/test_files/dir1/dir1_subdir3/alreadyUniq.txt"
            }
        )

    def test_tail_wrong_flag(self):
        with self.assertRaises(FlagError):
            eval(f"head -k 1 {self.file1}")

    @parameterized.expand(
        [
            # Empty File
            ("", empty, [""]),
            # Multiple lines file - takes numeric sorting into consideration
            (
                "",
                "test/test_files/dir1/dir1_subdir3/forUniq.txt",
                ["Apple", "apple", "banana", "apple", "banana",
                 "banAna", "Orange"],
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
    def test_uniq(self, case_insensitive, file, expected_result):
        out = eval(f"uniq {case_insensitive} {file}")
        result = out.popleft().strip().split("\n")
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
                ["Apple", "apple", "banana", "apple", "banana",
                 "banAna", "Orange"],
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
    def test_uniq_stdIn(self, case_insensitive, file, expected_result):
        out = eval(f"uniq {case_insensitive} < {file}")
        result = out.popleft().strip().split("\n")
        self.assertEqual(result, expected_result)

    def test_uniq_file_not_exists(self):
        with self.assertRaises(FlagError):
            eval("uniq wrongFile.txt")

    def test_uniq_no_args(self):
        with self.assertRaises(FlagError):
            eval("uniq")

    def test_uniq_wrong_flag(self):
        with self.assertRaises(FlagError):
            eval(f"uniq -f {self.file1}")

    def test_redir_both(self):
        eval(f"head -n 2 < {self.file1} > out.txt")
        result = File("out.txt").read().strip().split("\n")
        self.assertEqual(result, self.file1_content[:2])

    def test_redir_infront_cat(self):
        out = eval(f"< {self.file1} cat")
        result = out.popleft().strip().split("\n")
        self.assertEqual(result, self.file1_content)

    def test_pipe_cat_head(self):
        out = eval(f"cat {self.file1} | head -n 2")
        result = out.popleft().strip().split("\n")
        self.assertEqual(result, self.file1_content[:2])

    def test_pipe_cat_tail(self):
        out = eval(f"cat {self.file1} | tail -n 2")
        result = out.popleft().strip().split("\n")
        self.assertEqual(result, self.file1_content[-2:])

    def test_pipe_echo_cut(self):
        out = eval("echo abc | cut -b 1")
        result = out.popleft().strip()
        self.assertEqual(result, "a")

    def test_unsafe_command_not_exists(self):
        out = eval("_wrong")
        result = out.popleft().strip()
        self.assertEqual(result, "Error: Command Not Found")

    def test_cd_no_args(self):
        out = eval("cd; pwd")
        result = out.popleft().strip().split("\n")
        self.assertEqual(result, [os.getcwd()])

    def test_cut_invalid_byte(self):
        with self.assertRaises(InvalidFormatError):
            eval(f"cut -b a,3 {self.file1}")

    def test_find_too_many_args(self):
        with self.assertRaises(FlagError):
            eval(f"find {self.test_files_dir} -name -hello -hi 'file.txt'")

    def test_grep_too_many_args(self):
        with self.assertRaises(FlagError):
            eval(f"grep A... B... {self.file1} {self.file2}")

    def test_head_stdIn(self):
        out = eval(f"head < {self.file1}")
        result = out.popleft().strip().split("\n")
        self.assertEqual(result, self.file1_content)

    def test_head_default_n(self):
        out = eval(f"head {self.file1}")
        result = out.popleft().strip().split("\n")
        self.assertEqual(result, self.file1_content)

    def test_ls_no_args(self):
        eval("cd test/test_files")
        out = eval("ls")
        result = out.popleft().strip().split("\t")
        eval("cd /comp0010")
        result = set(result)
        self.assertEqual(result, {"dir1", "file2.txt",
                                  "empty.txt", "file1.txt"})

    def test_ls_too_many_args(self):
        with self.assertRaises(FlagError):
            eval("ls test test/test_files")

    def test_grep_no_args(self):
        with self.assertRaises(FlagError):
            eval("grep")

    def test_tail_stdIn(self):
        out = eval(f"tail < {self.file1}")
        result = out.popleft().strip().split("\n")
        self.assertEqual(result, self.file1_content)

    def test_tail_default_n(self):
        out = eval(f"tail {self.file1}")
        result = out.popleft().strip().split("\n")
        self.assertEqual(result, self.file1_content)

    def test_tail_too_many_args(self):
        with self.assertRaises(FlagError):
            eval(f"tail -n -j 3 {self.file1}")

    def test_head_unsafe_stdIn(self):
        out = eval(f"_head < {self.file1}")
        result = out.popleft().strip().split("\n")
        self.assertEqual(result, self.file1_content)

    def test_head_unsafe_stdIn_not_exists(self):
        out = eval("_head < wrongFile.txt")
        result = out.popleft().strip().split("\n")
        msg = "Error: 'wrongFile.txt': No such file or directory"
        self.assertEqual(result, [msg])

    def test_echo_sub(self):
        out = eval("echo a`echo a`a")
        result = out.popleft().strip().split("\n")
        self.assertEqual(result, ["aaa"])

    def test_wc(self):
        out = eval(f"wc {self.file1}")
        result = out.popleft().strip().split("\n")
        self.assertEqual(result, ['3 3 18'])

    def test_wc_l(self):
        out = eval(f"wc -l {self.file2}")
        result = out.popleft().strip().split("\n")
        self.assertEqual(result, ['4'])

    def test_wc_w(self):
        out = eval(f"wc -w {self.file2}")
        result = out.popleft().strip().split("\n")
        self.assertEqual(result, ['4'])

    def test_wc_m(self):
        out = eval(f"wc -m {self.file1} {self.file2}")
        result = out.popleft().strip().split("\n")
        self.assertEqual(result, ['37'])

    def test_wc_wrong_flag(self):
        with self.assertRaises(FlagError):
            eval(f"wc -f {self.file1} {self.file2}")

    def test_wc_no_arg(self):
        with self.assertRaises(FlagError):
            eval("wc")

    def test_wc_stdin(self):
        out = eval(f"wc -l < {self.file1}")
        result = out.popleft().strip().split("\n")
        self.assertEqual(result, ['3'])

    def test_wc_no_arg_stdin(self):
        out = eval(f"wc < {self.file1}")
        result = out.popleft().strip().split("\n")
        self.assertEqual(result, ['3 3 18'])

    def test_mkdir(self):
        out = eval("mkdir mkdir_test; ls")
        result = out.popleft().strip().split("\t")
        self.assertTrue("mkdir_test" in result)

    def test_mkdir_multiple(self):
        out = eval("mkdir -p mkdir_test1 mkdir_test2; ls")
        result = out.popleft().strip().split("\t")
        self.assertTrue(set(['mkdir_test1', 'mkdir_test2']).issubset(result))

    def test_mkdir_already_exists(self):
        with self.assertRaises(FileAlreadyExistsError):
            eval("mkdir test")

    def test_mkdir_missing_operand(self):
        with self.assertRaises(FlagError):
            eval("mkdir")

    def test_mkdir_p(self):
        with self.assertRaises(FlagError):
            eval("mkdir -p")

    def test_mkdir_missing_p(self):
        with self.assertRaises(FlagError):
            eval("mkdir a/b")

    def test_redir_in_front_unsafe(self):
        out = eval(f"< {self.file1} _head")
        result = out.popleft().strip().split("\n")
        self.assertEqual(result, self.file1_content)

    def test_shell_main(self):
        with patch("sys.argv", new=["script_name", "-c", "echo"]):
            with patch("sys.stdout", new_callable=io.StringIO) as mstdO:
                main()
                self.assertEqual(mstdO.getvalue().strip(), "")

    def test_shell_main_ValueError_0(self):
        with patch("sys.argv", new=["script_name", "echo foo bar", "-c"]):
            with patch("sys.stdout", new_callable=io.StringIO):
                with self.assertRaises(ValueError):
                    main()

    def test_shell_main_ValueError_1(self):
        with patch("sys.argv", new=["script_name", "-c",
                                    "echo foo", "echo ss"]):
            with patch("sys.stdout", new_callable=io.StringIO):
                with self.assertRaises(ValueError):
                    main()

    @patch("builtins.input", return_value="echo")
    @patch("builtins.print")
    def test_interactive_mode(self, mock_input, mock_print):
        with io.StringIO() as buf, patch("sys.stdout", buf):
            interactive_mode()
            output = buf.getvalue()
        expected_output = ""
        self.assertIn(expected_output, output)


if __name__ == "__main__":
    unittest.main()
