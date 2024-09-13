# Generated from shellParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,19,111,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,3,0,32,8,0,1,0,1,0,1,1,1,1,1,1,5,1,39,8,1,10,1,12,
        1,42,9,1,1,2,1,2,1,3,1,3,1,3,5,3,49,8,3,10,3,12,3,52,9,3,1,4,5,4,
        55,8,4,10,4,12,4,58,9,4,1,4,1,4,5,4,62,8,4,10,4,12,4,65,9,4,1,5,
        1,5,3,5,69,8,5,1,6,1,6,3,6,73,8,6,1,7,1,7,1,7,1,7,3,7,79,8,7,1,8,
        1,8,1,8,3,8,84,8,8,1,9,1,9,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,
        11,1,12,1,12,5,12,98,8,12,10,12,12,12,101,9,12,1,13,1,13,1,13,1,
        13,1,14,1,14,1,14,1,14,1,14,0,0,15,0,2,4,6,8,10,12,14,16,18,20,22,
        24,26,28,0,0,107,0,31,1,0,0,0,2,35,1,0,0,0,4,43,1,0,0,0,6,45,1,0,
        0,0,8,56,1,0,0,0,10,68,1,0,0,0,12,72,1,0,0,0,14,78,1,0,0,0,16,83,
        1,0,0,0,18,85,1,0,0,0,20,87,1,0,0,0,22,91,1,0,0,0,24,99,1,0,0,0,
        26,102,1,0,0,0,28,106,1,0,0,0,30,32,3,2,1,0,31,30,1,0,0,0,31,32,
        1,0,0,0,32,33,1,0,0,0,33,34,5,0,0,1,34,1,1,0,0,0,35,40,3,4,2,0,36,
        37,5,3,0,0,37,39,3,4,2,0,38,36,1,0,0,0,39,42,1,0,0,0,40,38,1,0,0,
        0,40,41,1,0,0,0,41,3,1,0,0,0,42,40,1,0,0,0,43,44,3,6,3,0,44,5,1,
        0,0,0,45,50,3,8,4,0,46,47,5,2,0,0,47,49,3,8,4,0,48,46,1,0,0,0,49,
        52,1,0,0,0,50,48,1,0,0,0,50,51,1,0,0,0,51,7,1,0,0,0,52,50,1,0,0,
        0,53,55,3,14,7,0,54,53,1,0,0,0,55,58,1,0,0,0,56,54,1,0,0,0,56,57,
        1,0,0,0,57,59,1,0,0,0,58,56,1,0,0,0,59,63,3,10,5,0,60,62,3,12,6,
        0,61,60,1,0,0,0,62,65,1,0,0,0,63,61,1,0,0,0,63,64,1,0,0,0,64,9,1,
        0,0,0,65,63,1,0,0,0,66,69,3,16,8,0,67,69,3,18,9,0,68,66,1,0,0,0,
        68,67,1,0,0,0,69,11,1,0,0,0,70,73,3,14,7,0,71,73,3,10,5,0,72,70,
        1,0,0,0,72,71,1,0,0,0,73,13,1,0,0,0,74,75,5,7,0,0,75,79,3,10,5,0,
        76,77,5,8,0,0,77,79,3,10,5,0,78,74,1,0,0,0,78,76,1,0,0,0,79,15,1,
        0,0,0,80,84,3,20,10,0,81,84,3,22,11,0,82,84,3,28,14,0,83,80,1,0,
        0,0,83,81,1,0,0,0,83,82,1,0,0,0,84,17,1,0,0,0,85,86,5,9,0,0,86,19,
        1,0,0,0,87,88,5,10,0,0,88,89,5,11,0,0,89,90,5,12,0,0,90,21,1,0,0,
        0,91,92,5,13,0,0,92,93,3,24,12,0,93,94,5,14,0,0,94,23,1,0,0,0,95,
        98,5,15,0,0,96,98,3,26,13,0,97,95,1,0,0,0,97,96,1,0,0,0,98,101,1,
        0,0,0,99,97,1,0,0,0,99,100,1,0,0,0,100,25,1,0,0,0,101,99,1,0,0,0,
        102,103,5,16,0,0,103,104,5,17,0,0,104,105,5,18,0,0,105,27,1,0,0,
        0,106,107,5,19,0,0,107,108,5,17,0,0,108,109,5,18,0,0,109,29,1,0,
        0,0,11,31,40,50,56,63,68,72,78,83,97,99
    ]

class shellParser ( Parser ):

    grammarFileName = "shellParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'|'", "';'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'<'", "'>'" ]

    symbolicNames = [ "<INVALID>", "WS", "PIPE", "SEMICOLON", "SINGLE_QUOTED", 
                      "DOUBLE_QUOTED", "BACKQUOTED", "REDIRECT_INPUT", "REDIRECT_OUTPUT", 
                      "UNQUOTED", "SQ_START", "SQ_CONTENT", "SQ_END", "DQ_START", 
                      "DQ_END", "DQ_CONTENT", "BQ_START_IN_DQ", "BQ_CONTENT", 
                      "BQ_END", "BQ_START" ]

    RULE_cmdline = 0
    RULE_commands = 1
    RULE_command = 2
    RULE_pipe = 3
    RULE_call = 4
    RULE_argument = 5
    RULE_atom = 6
    RULE_redirection = 7
    RULE_quoted = 8
    RULE_unquoted = 9
    RULE_singleQuoted = 10
    RULE_doubleQuoted = 11
    RULE_content = 12
    RULE_backQuotedInDoubleQuoted = 13
    RULE_backQuoted = 14

    ruleNames =  [ "cmdline", "commands", "command", "pipe", "call", "argument", 
                   "atom", "redirection", "quoted", "unquoted", "singleQuoted", 
                   "doubleQuoted", "content", "backQuotedInDoubleQuoted", 
                   "backQuoted" ]

    EOF = Token.EOF
    WS=1
    PIPE=2
    SEMICOLON=3
    SINGLE_QUOTED=4
    DOUBLE_QUOTED=5
    BACKQUOTED=6
    REDIRECT_INPUT=7
    REDIRECT_OUTPUT=8
    UNQUOTED=9
    SQ_START=10
    SQ_CONTENT=11
    SQ_END=12
    DQ_START=13
    DQ_END=14
    DQ_CONTENT=15
    BQ_START_IN_DQ=16
    BQ_CONTENT=17
    BQ_END=18
    BQ_START=19

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CmdlineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(shellParser.EOF, 0)

        def commands(self):
            return self.getTypedRuleContext(shellParser.CommandsContext,0)


        def getRuleIndex(self):
            return shellParser.RULE_cmdline

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCmdline" ):
                return visitor.visitCmdline(self)
            else:
                return visitor.visitChildren(self)




    def cmdline(self):

        localctx = shellParser.CmdlineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_cmdline)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 534400) != 0):
                self.state = 30
                self.commands()


            self.state = 33
            self.match(shellParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(shellParser.CommandContext)
            else:
                return self.getTypedRuleContext(shellParser.CommandContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(shellParser.SEMICOLON)
            else:
                return self.getToken(shellParser.SEMICOLON, i)

        def getRuleIndex(self):
            return shellParser.RULE_commands

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommands" ):
                return visitor.visitCommands(self)
            else:
                return visitor.visitChildren(self)




    def commands(self):

        localctx = shellParser.CommandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_commands)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.command()
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 36
                self.match(shellParser.SEMICOLON)
                self.state = 37
                self.command()
                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pipe(self):
            return self.getTypedRuleContext(shellParser.PipeContext,0)


        def getRuleIndex(self):
            return shellParser.RULE_command

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommand" ):
                return visitor.visitCommand(self)
            else:
                return visitor.visitChildren(self)




    def command(self):

        localctx = shellParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_command)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.pipe()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PipeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def call(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(shellParser.CallContext)
            else:
                return self.getTypedRuleContext(shellParser.CallContext,i)


        def PIPE(self, i:int=None):
            if i is None:
                return self.getTokens(shellParser.PIPE)
            else:
                return self.getToken(shellParser.PIPE, i)

        def getRuleIndex(self):
            return shellParser.RULE_pipe

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPipe" ):
                return visitor.visitPipe(self)
            else:
                return visitor.visitChildren(self)




    def pipe(self):

        localctx = shellParser.PipeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_pipe)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.call()
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 46
                self.match(shellParser.PIPE)
                self.state = 47
                self.call()
                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument(self):
            return self.getTypedRuleContext(shellParser.ArgumentContext,0)


        def redirection(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(shellParser.RedirectionContext)
            else:
                return self.getTypedRuleContext(shellParser.RedirectionContext,i)


        def atom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(shellParser.AtomContext)
            else:
                return self.getTypedRuleContext(shellParser.AtomContext,i)


        def getRuleIndex(self):
            return shellParser.RULE_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall" ):
                return visitor.visitCall(self)
            else:
                return visitor.visitChildren(self)




    def call(self):

        localctx = shellParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7 or _la==8:
                self.state = 53
                self.redirection()
                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 59
            self.argument()
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 534400) != 0):
                self.state = 60
                self.atom()
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def quoted(self):
            return self.getTypedRuleContext(shellParser.QuotedContext,0)


        def unquoted(self):
            return self.getTypedRuleContext(shellParser.UnquotedContext,0)


        def getRuleIndex(self):
            return shellParser.RULE_argument

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument" ):
                return visitor.visitArgument(self)
            else:
                return visitor.visitChildren(self)




    def argument(self):

        localctx = shellParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_argument)
        try:
            self.state = 68
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10, 13, 19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.quoted()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.unquoted()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def redirection(self):
            return self.getTypedRuleContext(shellParser.RedirectionContext,0)


        def argument(self):
            return self.getTypedRuleContext(shellParser.ArgumentContext,0)


        def getRuleIndex(self):
            return shellParser.RULE_atom

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = shellParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_atom)
        try:
            self.state = 72
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 70
                self.redirection()
                pass
            elif token in [9, 10, 13, 19]:
                self.enterOuterAlt(localctx, 2)
                self.state = 71
                self.argument()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RedirectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REDIRECT_INPUT(self):
            return self.getToken(shellParser.REDIRECT_INPUT, 0)

        def argument(self):
            return self.getTypedRuleContext(shellParser.ArgumentContext,0)


        def REDIRECT_OUTPUT(self):
            return self.getToken(shellParser.REDIRECT_OUTPUT, 0)

        def getRuleIndex(self):
            return shellParser.RULE_redirection

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRedirection" ):
                return visitor.visitRedirection(self)
            else:
                return visitor.visitChildren(self)




    def redirection(self):

        localctx = shellParser.RedirectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_redirection)
        try:
            self.state = 78
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self.match(shellParser.REDIRECT_INPUT)
                self.state = 75
                self.argument()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 76
                self.match(shellParser.REDIRECT_OUTPUT)
                self.state = 77
                self.argument()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuotedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def singleQuoted(self):
            return self.getTypedRuleContext(shellParser.SingleQuotedContext,0)


        def doubleQuoted(self):
            return self.getTypedRuleContext(shellParser.DoubleQuotedContext,0)


        def backQuoted(self):
            return self.getTypedRuleContext(shellParser.BackQuotedContext,0)


        def getRuleIndex(self):
            return shellParser.RULE_quoted

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuoted" ):
                return visitor.visitQuoted(self)
            else:
                return visitor.visitChildren(self)




    def quoted(self):

        localctx = shellParser.QuotedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_quoted)
        try:
            self.state = 83
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                self.singleQuoted()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 81
                self.doubleQuoted()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 3)
                self.state = 82
                self.backQuoted()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnquotedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UNQUOTED(self):
            return self.getToken(shellParser.UNQUOTED, 0)

        def getRuleIndex(self):
            return shellParser.RULE_unquoted

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnquoted" ):
                return visitor.visitUnquoted(self)
            else:
                return visitor.visitChildren(self)




    def unquoted(self):

        localctx = shellParser.UnquotedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_unquoted)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(shellParser.UNQUOTED)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SingleQuotedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SQ_START(self):
            return self.getToken(shellParser.SQ_START, 0)

        def SQ_CONTENT(self):
            return self.getToken(shellParser.SQ_CONTENT, 0)

        def SQ_END(self):
            return self.getToken(shellParser.SQ_END, 0)

        def getRuleIndex(self):
            return shellParser.RULE_singleQuoted

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingleQuoted" ):
                return visitor.visitSingleQuoted(self)
            else:
                return visitor.visitChildren(self)




    def singleQuoted(self):

        localctx = shellParser.SingleQuotedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_singleQuoted)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(shellParser.SQ_START)
            self.state = 88
            self.match(shellParser.SQ_CONTENT)
            self.state = 89
            self.match(shellParser.SQ_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DoubleQuotedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DQ_START(self):
            return self.getToken(shellParser.DQ_START, 0)

        def content(self):
            return self.getTypedRuleContext(shellParser.ContentContext,0)


        def DQ_END(self):
            return self.getToken(shellParser.DQ_END, 0)

        def getRuleIndex(self):
            return shellParser.RULE_doubleQuoted

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDoubleQuoted" ):
                return visitor.visitDoubleQuoted(self)
            else:
                return visitor.visitChildren(self)




    def doubleQuoted(self):

        localctx = shellParser.DoubleQuotedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_doubleQuoted)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(shellParser.DQ_START)
            self.state = 92
            self.content()
            self.state = 93
            self.match(shellParser.DQ_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DQ_CONTENT(self, i:int=None):
            if i is None:
                return self.getTokens(shellParser.DQ_CONTENT)
            else:
                return self.getToken(shellParser.DQ_CONTENT, i)

        def backQuotedInDoubleQuoted(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(shellParser.BackQuotedInDoubleQuotedContext)
            else:
                return self.getTypedRuleContext(shellParser.BackQuotedInDoubleQuotedContext,i)


        def getRuleIndex(self):
            return shellParser.RULE_content

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContent" ):
                return visitor.visitContent(self)
            else:
                return visitor.visitChildren(self)




    def content(self):

        localctx = shellParser.ContentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_content)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15 or _la==16:
                self.state = 97
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [15]:
                    self.state = 95
                    self.match(shellParser.DQ_CONTENT)
                    pass
                elif token in [16]:
                    self.state = 96
                    self.backQuotedInDoubleQuoted()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 101
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BackQuotedInDoubleQuotedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BQ_START_IN_DQ(self):
            return self.getToken(shellParser.BQ_START_IN_DQ, 0)

        def BQ_CONTENT(self):
            return self.getToken(shellParser.BQ_CONTENT, 0)

        def BQ_END(self):
            return self.getToken(shellParser.BQ_END, 0)

        def getRuleIndex(self):
            return shellParser.RULE_backQuotedInDoubleQuoted

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBackQuotedInDoubleQuoted" ):
                return visitor.visitBackQuotedInDoubleQuoted(self)
            else:
                return visitor.visitChildren(self)




    def backQuotedInDoubleQuoted(self):

        localctx = shellParser.BackQuotedInDoubleQuotedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_backQuotedInDoubleQuoted)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(shellParser.BQ_START_IN_DQ)
            self.state = 103
            self.match(shellParser.BQ_CONTENT)
            self.state = 104
            self.match(shellParser.BQ_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BackQuotedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BQ_START(self):
            return self.getToken(shellParser.BQ_START, 0)

        def BQ_CONTENT(self):
            return self.getToken(shellParser.BQ_CONTENT, 0)

        def BQ_END(self):
            return self.getToken(shellParser.BQ_END, 0)

        def getRuleIndex(self):
            return shellParser.RULE_backQuoted

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBackQuoted" ):
                return visitor.visitBackQuoted(self)
            else:
                return visitor.visitChildren(self)




    def backQuoted(self):

        localctx = shellParser.BackQuotedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_backQuoted)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(shellParser.BQ_START)
            self.state = 107
            self.match(shellParser.BQ_CONTENT)
            self.state = 108
            self.match(shellParser.BQ_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





