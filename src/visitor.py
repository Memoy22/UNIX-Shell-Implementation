from antlr4 import CommonTokenStream, InputStream, ParseTreeVisitor

from parser.shellLexer import shellLexer
from parser.shellParser import shellParser


class ShellVisitor(ParseTreeVisitor):
    def visitCmdline(self, ctx: shellParser.CmdlineContext):
        return self.visit(ctx.commands())

    def visitCommands(self, ctx: shellParser.CommandsContext):
        command_results = [self.visit(command) for command in ctx.command()]
        return command_results

    def visitCommand(self, ctx: shellParser.CommandContext):
        return self.visit(ctx.pipe())

    def visitPipe(self, ctx: shellParser.PipeContext):
        commands = [self.visit(call) for call in ctx.call()]
        return commands

    def visitCall(self, ctx: shellParser.CallContext):
        """
        Visit a call node and return a dictionary with the call information.
        The dictionary will have the following keys:
        - cmd: The command to be executed
        - arguments: A list of arguments to be passed to the command
        - subcommands: A list of subcommands to be executed
        - inputFile: The file to be used as input
        - outputFile: The file to be used as output
        """
        cmd = self.visit(ctx.cmd()) if ctx.cmd() else None
        arguments = [self.visit(arg) for arg in ctx.argument()] or None
        subcommands = [self.visit(subcmd) for subcmd in
                       ctx.subcommand()] or None
        inputFile, outputFile = self.getRedirections(ctx)

        call = {
            "cmd": cmd,
            "arguments": arguments,
            "subcommands": subcommands,
            "inputFile": inputFile,
            "outputFile": outputFile,
        }
        if call["cmd"] is None and call["inputFile"] is not None:
            call["cmd"] = "<"
            call["arguments"] = [call["inputFile"]]
            call["inputFile"] = None

        return call

    def getRedirections(self, ctx):
        """Get the input and output files for the call."""
        redirections = self.handleRedirection(ctx)

        inputFile = [
                        redirection[1] for redirection in redirections if
                        redirection[0] == "<"
                    ] or None
        outputFile = [
                         redirection[1] for redirection in redirections if
                         redirection[0] == ">"
                     ] or None

        inputFile = (
            inputFile[0] if inputFile is not None and len(
                inputFile) == 1 else inputFile
        )
        outputFile = (
            outputFile[0]
            if outputFile is not None and len(outputFile) == 1
            else outputFile
        )
        return inputFile, outputFile

    def handleRedirection(self, ctx: shellParser.CallContext):
        """
        Handle redirections in the call.
        Redirections can be in the beginning of the call or in the middle of the call.
        """
        redirections = []

        for child in ctx.children:
            # To handle redirection in beginning like '> hi.txt'
            if isinstance(child, shellParser.RedirectionContext):
                redirection_ctx = child
                redirection = self.visit(
                    redirection_ctx) if redirection_ctx else None
                redirections.append(redirection)
                break
            # To handle usual redirection cases
            elif isinstance(child, shellParser.AtomContext):
                for atom_child in child.children:
                    if isinstance(atom_child, shellParser.RedirectionContext):
                        redirection_ctx = atom_child
                        redirection = (
                            self.visit(
                                redirection_ctx) if redirection_ctx else None
                        )
                        redirections.append(redirection)
                        break
        return redirections

    def visitCmd(self, ctx: shellParser.CmdContext):
        if ctx.SINGLE_QUOTED():
            return ctx.SINGLE_QUOTED().getText()[1:-1]
        elif ctx.DOUBLE_QUOTED():
            return ctx.DOUBLE_QUOTED().getText()[1:-1]
        elif ctx.BACKQUOTED():
            return ctx.BACKQUOTED().getText()
        elif ctx.UNQUOTED():
            return ctx.UNQUOTED().getText()
        else:
            return self.visit(ctx.redirection())

    def visitSubcommand(self, ctx: shellParser.SubcommandContext):
        return self.visit(ctx.commands())

    def visitArgument(self, ctx: shellParser.ArgumentContext):
        arguments = []

        for arg in ctx.children:
            if isinstance(arg, shellParser.QuotedContext):
                arguments.append(self.visit(arg))
            elif isinstance(arg, shellParser.UnquotedContext):
                unquoted_arg = self.visit(arg)
                arguments.append(unquoted_arg)
        return arguments

    @staticmethod
    def visitUnquoted(ctx: shellParser.UnquotedContext):
        """
        Return the unquoted text from the context.
        This method removes the quotes from the unquoted text.
        """
        uq = ctx.UNQUOTED().getText()
        if uq[0] == '"' or uq[0] == "'":
            uq = uq[1:]
        if '"' in uq:
            new_uq = ""
            for char in uq:
                if char != '"':
                    new_uq += char
            uq = new_uq
        return uq

    @staticmethod
    def visitQuoted(ctx: shellParser.QuotedContext):
        if ctx.SINGLE_QUOTED():
            return ctx.SINGLE_QUOTED().getText()
        elif ctx.DOUBLE_QUOTED():
            return ctx.DOUBLE_QUOTED().getText()[1:-1]
        elif ctx.BACKQUOTED():
            return ctx.BACKQUOTED().getText()

    def visitRedirection(self, ctx: shellParser.RedirectionContext):
        redirect_type = ctx.children[0].getText()
        argument = self.visit(ctx.argument())
        return redirect_type, argument

    @staticmethod
    def converter(string_to_parse):
        """
        Convert a string to a list of dictionaries with the call information.
        The string is parsed using the shell grammar and the visitor pattern.
        """
        input_stream = InputStream(string_to_parse)
        lexer = shellLexer(input_stream)
        tokens = CommonTokenStream(lexer)
        parser = shellParser(tokens)
        tree = parser.cmdline()
        custom_visitor = ShellVisitor()
        result = custom_visitor.visit(tree)
        return result

    @staticmethod
    def filter_args(call_list, echo_flag):
        """
        Filter the arguments from the call list.
        If the echo_flag is True, the arguments are returned as they are.
        If the echo_flag is False, the arguments are returned without the quotes.
        """
        if call_list is None:
            return
        res = [arg for arg in call_list[0] if arg]
        if not echo_flag:
            temp = []
            for arg in res:
                if arg[0] == arg[-1] == "'":
                    temp.append(arg[1:-1])
                else:
                    temp.append(arg)
            res = temp
        return res

    def clean_args(self, cmd_line):
        """
        Clean the arguments in the command line.
        The arguments are cleaned by removing the quotes from the arguments.
        """
        for command in cmd_line:
            for call_dict in command:
                echo_flag = True if call_dict["cmd"] == "echo" else False
                call_dict["arguments"] = self.filter_args(
                    call_dict["arguments"], echo_flag
                )
        return cmd_line

    def get_sub_call(self, cmd_line):
        """
        Get the subcommands from the command line.
        The subcommands are stored in the subcommands key of the call dictionary.
        """
        for command in cmd_line:
            for call_dict in command:
                if call_dict["arguments"] is not None:
                    for index, args in enumerate(call_dict["arguments"]):
                        if len(args) > 0 and args[0] == args[-1] == "`":
                            sub_cmdline = self.converter(args[1:-1])
                            sub_cmdline = self.clean_args(sub_cmdline)
                            call_dict["subcommands"] = {}
                            call_dict["subcommands"][index] = sub_cmdline
        return cmd_line

    def get_cmd_get_call(self, call_dict):
        """
        Get the command from a sub call.
        The command is stored in the cmd key of the call dictionary.
        """
        cmd_from_sub_call = self.converter(call_dict["cmd"][1:-1])
        cmd_from_sub_call = self.clean_args(cmd_from_sub_call)
        call_dict["cmd"] = cmd_from_sub_call

    def get_dict_from_sub_call(self, call_dict):
        """
        Get the call dictionary from a sub call.
        """
        if call_dict["cmd"] is not None:
            if (
                    len(call_dict["cmd"]) > 0
                    and call_dict["cmd"][0] == call_dict["cmd"][-1] == "`"
            ):
                self.get_cmd_get_call(call_dict)
                return

    def get_cmd_from_sub_call_cmd(self, command):
        """ Get command dictionaries from sub call commands."""
        for call_dict in command:
            return self.get_dict_from_sub_call(call_dict)

    def get_cmd_from_sub_call(self, cmd_line):
        """ Get sub command dictionaries from call commands."""
        for command in cmd_line:
            self.get_cmd_from_sub_call_cmd(command)
        return cmd_line

    def get_call(self, command_string):
        """
        Get the call from the command string.
        The call is a list of dictionaries with the call information.
        """
        cmdline = self.converter(command_string)
        cmdline = self.clean_args(cmdline)
        cmdline = self.get_sub_call(cmdline)
        cmdline = self.get_cmd_from_sub_call(cmdline)
        return cmdline
