import io
import unittest
from unittest.mock import patch
from collections import deque
from exceptions import CommandNotFoundError
from shell import eval, interactive_mode, main


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

    def test_empty_cmdline(self, out=deque()):
        eval("", out)
        result = get_result(out)
        self.assertEqual(result, [""])

    def test_unsafe_command_not_exists(self, out=deque()):
        with self.assertRaises(CommandNotFoundError):
            eval("_wrong", out)

    def test_shell_main(self, out=deque()):
        with patch("sys.argv", new=["script_name", "-c", "echo"]):
            with patch("sys.stdout", new_callable=io.StringIO) as stdO:
                main()
                self.assertEqual(stdO.getvalue().strip(), "")

    def test_shell_main_ValueError_0(self, out=deque()):
        with patch("sys.argv", new=["script_name", "echo foo bar", "-c"]):
            with patch("sys.stdout", new_callable=io.StringIO):
                with self.assertRaises(ValueError):
                    main()

    def test_shell_main_ValueError_1(self, out=deque()):
        with patch(
                "sys.argv",
                new=[
                    "script_name",
                    "-c",
                    "echo foo",
                    "echo ss"
                ]
        ):
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
