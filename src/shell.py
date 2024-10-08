from visitor import ShellVisitor
from collections import deque
import sys
import os


def eval(cmdline, out):
    if not cmdline:
        return

    return ShellVisitor.converter(cmdline).execute(out)


def non_interactive_mode(args):
    if len(args) - 1 != 2:
        raise ValueError("wrong number of command line arguments")
    if args[1] != "-c":
        raise ValueError(f"unexpected command line argument {args[1]}")
    out = deque()
    eval(args[2], out)
    while len(out) > 0:
        print(out.popleft(), end="")


def interactive_mode():
    out = deque()
    print(os.getcwd() + "> ", end="")
    eval(input(), out)

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
