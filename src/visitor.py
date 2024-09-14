from antlr4 import CommonTokenStream, InputStream, ParseTreeVisitor
from parser.shellLexer import shellLexer
from parser.shellParser import shellParser
from structure_commands.pipe import Pipe
from structure_commands.seq import Seq
from structure_commands.call import Call


def visitSingleQuoted(ctx: shellParser.SingleQuotedContext):
    return ctx.SQ_CONTENT().getText()


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

    def visitCommand(self, ctx: shellParser.CommandContext):
        return self.visitPipe(ctx.pipe())

    def visitPipe(self, ctx: shellParser.PipeContext):
        left_command = self.visitCall(ctx.call(0))

        for i in range(1, len(ctx.call())):
            right_command = self.visitCall(ctx.call(i))
            left_command = Pipe(left=left_command, right=right_command)

        return left_command

    def visitCall(self, ctx: shellParser.CallContext):
        cmd = self.visitArgument(ctx.argument()) if ctx.argument() else None
        arguments = None
        stdin = None
        stdout = None

        for redirection in ctx.redirection():
            redir, arg = self.visitRedirection(redirection)
            if redir == "stdin":
                stdin = arg
            else:
                stdout = arg

        for atom in ctx.atom():
            if atom.redirection():
                redir, arg = self.visitRedirection(atom.redirection())
                if redir == "stdin":
                    stdin = arg
                else:
                    stdout = arg
            else:
                argument = self.visitArgument(atom.argument())
                if isinstance(argument, list):
                    arguments.extend(argument)
                else:
                    arguments.append(argument)

        return Call(cmd=cmd, arguments=arguments, stdin=stdin, stdout=stdout)

    def visitArgument(self, ctx: shellParser.ArgumentContext):
        if ctx.quoted():
            return self.visitQuoted(ctx.quoted())
        else:
            return self.visitUnquoted(ctx.unquoted())

    def visitQuoted(self, ctx: shellParser.QuotedContext):
        if ctx.singleQuoted():
            return visitSingleQuoted(ctx.singleQuoted())
        elif ctx.doubleQuoted():
            return self.visitDoubleQuoted(ctx.doubleQuoted())
        else:
            return self.visitBackQuoted(ctx.backQuoted())

    def visitDoubleQuoted(self, ctx: shellParser.DoubleQuotedContext):
        return self.visitContent(ctx.content())

    def visitContent(self, ctx: shellParser.ContentContext):
        res = []
        for child in ctx.getChildren():
            if isinstance(child, shellParser.BackQuotedInDoubleQuotedContext):
                res.extend(self.visitBackQuotedInDoubleQuoted(child))
            else:
                res.append(child.getText())
        return res

    def visitBackQuotedInDoubleQuoted(
            self,
            ctx: shellParser.BackQuotedInDoubleQuotedContext
    ):
        content = []
        for child in ctx.getChildren():
            bq_text = child.getText()
            # Handle terminal nodes like `BQ_START_IN_DQ` and `BQ_END`
            if bq_text == "`":
                continue
            content.append(self.visitBackQuoted(child))
        return content

    def visitBackQuoted(self, ctx: shellParser.BackQuotedContext):
        bq_text = ctx.getText()
        if bq_text[0] == bq_text[-1] == "`":
            return self.converter(bq_text[1:-1])
        return self.converter(ctx.getText())

    @staticmethod
    def visitUnquoted(ctx: shellParser.UnquotedContext):
        return ctx.UNQUOTED().getText()

    def visitRedirection(self, ctx: shellParser.RedirectionContext):
        if ctx.REDIRECT_INPUT():
            return "stdin", self.visitArgument(ctx.argument())
        elif ctx.REDIRECT_OUTPUT():
            return "stdout", self.visitArgument(ctx.argument())

    @staticmethod
    def converter(input_stream):
        input_stream = InputStream(input_stream)
        lexer = shellLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = shellParser(token_stream)
        tree = parser.cmdline()

        visitor = ShellVisitor()
        res = visitor.visit(tree)
        return res

