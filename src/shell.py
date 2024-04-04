from visitor import ShellVisitor
from handler import CommandHandler
import sys
import os


def eval(cmdline):
    """
    Evaluate the command line.
    Args:
        cmdline (str): The command line to evaluate.
    Returns:
        str: The output of the command line.
    """
    if not cmdline:
        return eval("echo")
    visitor = ShellVisitor()
    call = visitor.get_call(cmdline)

    handler = CommandHandler()
    handler.process_call(call)

    output = handler.get_out()
    return output


def non_interactive_mode(args):
    """ Run the shell in non-interactive mode. """

    if len(args) - 1 != 2:
        raise ValueError("wrong number of command line arguments")
    if args[1] != "-c":
        raise ValueError(f"unexpected command line argument {args[1]}")
    out = eval(args[2])
    while len(out) > 0:
        print(out.popleft(), end="")


def interactive_mode():
    """ Run the shell in interactive mode. """
    print(os.getcwd() + "> ", end="")
    out = eval(input())
    while len(out) > 0:
        print(out.popleft(), end="")


def main():
    args_num = len(sys.argv) - 1
    if args_num > 0:
        non_interactive_mode(sys.argv)
    else:
        while True:
            interactive_mode()


if __name__ == "__main__":
    main()
