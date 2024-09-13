# Generated from shellParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .shellParser import shellParser
else:
    from shellParser import shellParser

# This class defines a complete generic visitor for a parse tree produced by shellParser.

class shellParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by shellParser#cmdline.
    def visitCmdline(self, ctx:shellParser.CmdlineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by shellParser#commands.
    def visitCommands(self, ctx:shellParser.CommandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by shellParser#command.
    def visitCommand(self, ctx:shellParser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by shellParser#pipe.
    def visitPipe(self, ctx:shellParser.PipeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by shellParser#call.
    def visitCall(self, ctx:shellParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by shellParser#argument.
    def visitArgument(self, ctx:shellParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by shellParser#atom.
    def visitAtom(self, ctx:shellParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by shellParser#redirection.
    def visitRedirection(self, ctx:shellParser.RedirectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by shellParser#quoted.
    def visitQuoted(self, ctx:shellParser.QuotedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by shellParser#unquoted.
    def visitUnquoted(self, ctx:shellParser.UnquotedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by shellParser#singleQuoted.
    def visitSingleQuoted(self, ctx:shellParser.SingleQuotedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by shellParser#doubleQuoted.
    def visitDoubleQuoted(self, ctx:shellParser.DoubleQuotedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by shellParser#content.
    def visitContent(self, ctx:shellParser.ContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by shellParser#backQuotedInDoubleQuoted.
    def visitBackQuotedInDoubleQuoted(self, ctx:shellParser.BackQuotedInDoubleQuotedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by shellParser#backQuoted.
    def visitBackQuoted(self, ctx:shellParser.BackQuotedContext):
        return self.visitChildren(ctx)



del shellParser