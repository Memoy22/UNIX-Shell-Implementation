from antlr4 import CommonTokenStream, InputStream, ParseTreeVisitor
from parser.shellLexer import shellLexer
from parser.shellParser import shellParser
from structure_commands.pipe import Pipe
from structure_commands.seq import Seq
from structure_commands.call import Call


class ShellVisitor(ParseTreeVisitor):
    def visitCmdline(self, ctx: shellParser.CmdlineContext):
        if ctx.commands():
            return self.visitCommands(ctx.commands())
        return None

    def visitCommands(self, ctx: shellParser.CommandsContext):
        left_command = self.visitCommand(ctx.command(0))

        for i in range(1, len(ctx.command())):
            right_command = self.visitCommand(ctx.command(i))
            left_command = Seq(left=left_command, right=right_command)

        return left_command

    # Handling pipes by visiting the pipe within the command
    def visitCommand(self, ctx: shellParser.CommandContext):
        return self.visitPipe(ctx.pipe())

    def visitPipe(self, ctx: shellParser.PipeContext):
        left_command = self.visitCall(ctx.call(0))

        # Iterate over subsequent calls to handle pipes
        for i in range(1, len(ctx.call())):
            right_command = self.visitCall(ctx.call(i))
            left_command = Pipe(left=left_command, right=right_command)

        return left_command

    def visitCall(self, ctx: shellParser.CallContext):
        cmd = self.visitArgument(ctx.argument()) if ctx.argument() else None
        arguments = []
        stdin = None
        stdout = None

        # Visit and process redirections
        for redirection in ctx.redirection():
            redir, arg = self.visitRedirection(redirection)
            if redir == "stdin":
                stdin = arg
            else:
                stdout = arg

        # Process arguments and atoms
        for atom in ctx.atom():
            if atom.redirection():
                redir, arg = self.visitRedirection(atom.redirection())
                if redir == "stdin":
                    stdin = arg
                else:
                    stdout = arg
            else:
                arguments.append(self.visitArgument(atom.argument()))

        return Call(cmd=cmd, arguments=arguments, stdin=stdin, stdout=stdout)

    def visitArgument(self, ctx: shellParser.ArgumentContext):
        if ctx.quoted():
            return self.visitQuoted(ctx.quoted())
        else:
            return self.visitUnquoted(ctx.unquoted())

    def visitQuoted(self, ctx: shellParser.QuotedContext):
        if ctx.singleQuoted():
            return self.visitSingleQuoted(ctx.singleQuoted())
        elif ctx.doubleQuoted():
            return self.visitDoubleQuoted(ctx.doubleQuoted())
        else:
            return self.visitBackQuoted(ctx.backQuoted())

    def visitSingleQuoted(self, ctx: shellParser.SingleQuotedContext):
        return ctx.SQ_CONTENT().getText()

    def visitDoubleQuoted(self, ctx: shellParser.DoubleQuotedContext):
        return self.visitContent(ctx.content())

    def visitContent(self, ctx: shellParser.ContentContext):
        if ctx.DQ_CONTENT():
            return "".join(
                [dq_content.getText() for dq_content in ctx.DQ_CONTENT()])
        elif ctx.backQuotedInDoubleQuoted():
            return self.visitBackQuotedInDoubleQuoted(
                ctx.backQuotedInDoubleQuoted())
        return ""

    def visitBackQuotedInDoubleQuoted(self, ctx: shellParser.BackQuotedInDoubleQuotedContext):
        content = []
        if hasattr(ctx, 'children'):
            for child in ctx.children:
                content.append(
                    child.getText())  # Extract text for each child token
        return "`" + "".join(content) + "`"

    def visitBackQuoted(self, ctx: shellParser.BackQuotedContext):
        return "`" + ctx.BQ_CONTENT().getText() + "`"

    def visitUnquoted(self, ctx: shellParser.UnquotedContext):
        return ctx.UNQUOTED().getText()

    def visitRedirection(self, ctx: shellParser.RedirectionContext):
        if ctx.REDIRECT_INPUT():
            return "stdin", self.visitArgument(ctx.argument())
        elif ctx.REDIRECT_OUTPUT():
            return "stdout", self.visitArgument(ctx.argument())

    def converter(self, input_stream="echo foo bar"):
        input_stream = InputStream(input_stream)
        lexer = shellLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = shellParser(token_stream)
        tree = parser.cmdline()

        visitor = ShellVisitor()
        res = visitor.visit(tree)
        return res


if __name__ == "__main__":
    string = 'echo "`echo foo`"'
    visitor = ShellVisitor()
    result = visitor.converter(string)
    print(result)
