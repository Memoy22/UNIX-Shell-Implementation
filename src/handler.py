from collections import deque

from command_factory import CommandFactory
from exceptions import CommandNotFoundError
from exceptions import MultipleRedirectionError
from utils import File
from utils import Validator


class CommandHandler:
    def __init__(self):
        self.out = deque()

    def get_out(self):
        """
        Get the output of the command handler.
        Returns:
            deque: The output of the command handler.
        """
        return self.out

    def handle_substituted_cmd(self, sub_cmd):
        """
        This function handles the substituted command
        """
        return self.process_sub_call(sub_cmd)[0][0]

    def echo_sub(self, command_dict, dict_call, sub_output, index):
        """
        This function modifies the echo command when found in subcommand
        :param command_dict: dictionary of the command
        :param dict_call: list of command elements
        :param sub_output: output of the substituted command
        :param index: index of the substituted command
        :return: None
        """
        for sub_index in command_dict['subcommands']:
            if 0 < sub_index < len(dict_call[1]) - 1:
                dict_call[1] = self.get_new_arg_echo_sub(dict_call,
                                                         sub_output, sub_index)
            else:
                dict_call[1] = (dict_call[1][:index] + [f"'{arg[0]}'" for arg
                                                        in sub_output] +
                                dict_call[1][index + 1:])

    def handle_substituted_arg(self, command_dict, dict_call, sub_output,
                               index):
        if command_dict['cmd'] == 'echo':
            self.echo_sub(command_dict, dict_call, sub_output, index)
        else:
            dict_call[1] = dict_call[1][:index] + sub_output[0] + dict_call[1][
                                                                  index + 1:]

    def pipe(self, pipe, dict_call):
        """This function handles the pipe operation
        :param pipe: list of outputs from previous commands
        :param dict_call: list of command elements
        :return: None
        """
        if pipe and dict_call[2] is None:
            dict_call[2] = self.handle_pipe(pipe)

    def process(self, commands, out):
        """
        This function processes the commands and adds output to the out deque
        :param commands: list of commands
        :param out: list of outputs
        :return: None
        """
        for command in commands:
            pipe = []
            for command_dict in command:
                dict_call = self.get_handler_elements(command_dict)
                self.pipe(pipe, dict_call)

                if isinstance(command_dict['cmd'], list):
                    dict_call[0] = self.handle_substituted_cmd(
                        command_dict['cmd'])

                if command_dict['subcommands'] is not None:
                    for index in command_dict['subcommands']:
                        sub_call = command_dict['subcommands'][index]
                        sub_output = self.process_sub_call(sub_call)
                        self.handle_substituted_arg(command_dict, dict_call,
                                                    sub_output, index)

                output = self.run_call(dict_call)
                if dict_call[3] is not None and len(dict_call[3]) == 1:
                    File(dict_call[3][0]).write(output)
                else:
                    pipe.append(
                        output.strip() if output is not None else output)

            if pipe:
                out.append(
                    pipe[-1] + '\n' if pipe[-1] is not None else pipe[-1])

    def process_sub_call(self, commands):
        """ This function processes the sub call commands"""
        out = []
        self.process(commands, out)
        out = [line.strip('\n').split('\n') for line in out]
        return out

    def process_call(self, commands):
        """
        This function processes the call
        :param commands: list of commands
        """
        out = []
        self.process(commands, out)
        for output in out:
            if output is not None:
                self.out.append(output)

    def run_call(self, dict_call):
        """
        This function runs the command and returns the output
        :param dict_call: list of command elements
        :return: output of the command
        """
        cmd = dict_call[0]
        args = dict_call[1]
        stdIn = dict_call[2]
        stdOut = dict_call[3]

        if cmd == '<':
            cmd, args = self.run_redir_in_front(args)

        if cmd.startswith('_'):
            try:
                command = CommandFactory().get_command(cmd[1:])
                self.check_redir(stdIn, stdOut)
                return command.execute(args, stdIn)
            except CommandNotFoundError as e:
                return f"{e}\n"
            except MultipleRedirectionError as e:
                return f"{e}\n"
            except Exception as e:
                return f"{e}\n"

        else:
            command = CommandFactory().get_command(cmd)
            self.check_redir(stdIn, stdOut)
            return command.execute(args, stdIn)

    @staticmethod
    def get_handler_elements(command_dict):
        """
        This function returns the elements of the command
        :param command_dict: dictionary of the command
        :return: list of elements of the command
        """
        cmd = command_dict['cmd']
        args = command_dict['arguments']
        input_file = command_dict['inputFile']
        if input_file is not None and len(input_file) == 1:
            if Validator.check_path_exists_bool(input_file[0]):
                input_file = File(input_file[0]).read_lines()
            elif cmd.startswith('_'):
                input_file = input_file[0]
            else:
                Validator.check_path_exists(input_file[0])
        elif input_file is not None:
            input_file = 'raise_error'
        outputFile = command_dict['outputFile']
        return [cmd, args, input_file, outputFile]

    @staticmethod
    def handle_pipe(pipe):
        """
        This function handles the pipe operation
        :param pipe: list of outputs from previous commands
        :return: list of last output from the pipe split by \n
        """
        if pipe[-1] is not None:
            return pipe[-1].split('\n')
        return

    @staticmethod
    def get_new_arg_echo_sub(dict_call, sub_output, sub_index):
        """
        This function modifies the argument for echo command
        :param dict_call: list of command elements
        :param sub_output: output of the substituted command
        :param sub_index: index of the substituted command
        :return: list of modified argument
        """
        modified_arg = ""
        for arg in dict_call[1][:sub_index]:
            modified_arg += arg
        modified_arg += sub_output[0][0]
        for arg in dict_call[1][sub_index + 1:]:
            modified_arg += arg
        return [modified_arg]

    @staticmethod
    def run_redir_in_front(args):
        """
        This function handles the redirection in front of the command
        :param args: list of arguments
        :return: list of modified command and arguments
        """
        new_args = []
        for arg in args:
            if arg:
                if arg.startswith('_'):
                    if CommandFactory().is_command(arg[1:]):
                        cmd = arg
                elif CommandFactory().is_command(arg):
                    cmd = arg
                else:
                    new_args.append(arg)
        args = new_args
        try:
            return cmd, args
        except UnboundLocalError:
            raise CommandNotFoundError("Error: Command not found")

    @staticmethod
    def check_redir(stdin, stdout):
        """
        This function checks the redirections and
        raises errors if multiple redirections are given
        :param stdin: input redirection
        :param stdout: output redirection
        """
        stdin_error = "Error: Multiple Input Redirections given"
        stdout_error = "Error: Multiple Output Redirections given"
        if stdin == "raise_error":
            raise MultipleRedirectionError(stdin_error)
        elif isinstance(stdin, str):
            Validator.check_path_exists(stdin)
        if stdout is not None and len(stdout) != 1:
            raise MultipleRedirectionError(stdout_error)
