# Generated from shellParser.g4 by ANTLR 4.13.1
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
        4,1,9,110,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,3,0,26,8,0,1,0,
        1,0,1,1,1,1,1,1,3,1,33,8,1,5,1,35,8,1,10,1,12,1,38,9,1,1,2,1,2,1,
        3,1,3,1,3,5,3,45,8,3,10,3,12,3,48,9,3,1,4,1,4,3,4,52,8,4,1,4,5,4,
        55,8,4,10,4,12,4,58,9,4,1,4,1,4,1,4,5,4,63,8,4,10,4,12,4,66,9,4,
        1,4,5,4,69,8,4,10,4,12,4,72,9,4,1,5,1,5,1,6,1,6,1,7,1,7,3,7,80,8,
        7,1,8,1,8,4,8,84,8,8,11,8,12,8,85,1,9,1,9,1,10,1,10,1,11,1,11,5,
        11,94,8,11,10,11,12,11,97,9,11,1,11,1,11,1,11,5,11,102,8,11,10,11,
        12,11,105,9,11,1,11,3,11,108,8,11,1,11,0,0,12,0,2,4,6,8,10,12,14,
        16,18,20,22,0,2,2,0,4,6,9,9,1,0,4,6,113,0,25,1,0,0,0,2,29,1,0,0,
        0,4,39,1,0,0,0,6,41,1,0,0,0,8,51,1,0,0,0,10,73,1,0,0,0,12,75,1,0,
        0,0,14,79,1,0,0,0,16,83,1,0,0,0,18,87,1,0,0,0,20,89,1,0,0,0,22,107,
        1,0,0,0,24,26,3,2,1,0,25,24,1,0,0,0,25,26,1,0,0,0,26,27,1,0,0,0,
        27,28,5,0,0,1,28,1,1,0,0,0,29,36,3,4,2,0,30,32,5,3,0,0,31,33,3,4,
        2,0,32,31,1,0,0,0,32,33,1,0,0,0,33,35,1,0,0,0,34,30,1,0,0,0,35,38,
        1,0,0,0,36,34,1,0,0,0,36,37,1,0,0,0,37,3,1,0,0,0,38,36,1,0,0,0,39,
        40,3,6,3,0,40,5,1,0,0,0,41,46,3,8,4,0,42,43,5,2,0,0,43,45,3,8,4,
        0,44,42,1,0,0,0,45,48,1,0,0,0,46,44,1,0,0,0,46,47,1,0,0,0,47,7,1,
        0,0,0,48,46,1,0,0,0,49,52,3,10,5,0,50,52,3,22,11,0,51,49,1,0,0,0,
        51,50,1,0,0,0,52,56,1,0,0,0,53,55,5,1,0,0,54,53,1,0,0,0,55,58,1,
        0,0,0,56,54,1,0,0,0,56,57,1,0,0,0,57,64,1,0,0,0,58,56,1,0,0,0,59,
        63,3,16,8,0,60,63,3,14,7,0,61,63,3,12,6,0,62,59,1,0,0,0,62,60,1,
        0,0,0,62,61,1,0,0,0,63,66,1,0,0,0,64,62,1,0,0,0,64,65,1,0,0,0,65,
        70,1,0,0,0,66,64,1,0,0,0,67,69,5,1,0,0,68,67,1,0,0,0,69,72,1,0,0,
        0,70,68,1,0,0,0,70,71,1,0,0,0,71,9,1,0,0,0,72,70,1,0,0,0,73,74,7,
        0,0,0,74,11,1,0,0,0,75,76,5,6,0,0,76,13,1,0,0,0,77,80,3,22,11,0,
        78,80,3,16,8,0,79,77,1,0,0,0,79,78,1,0,0,0,80,15,1,0,0,0,81,84,3,
        20,10,0,82,84,3,18,9,0,83,81,1,0,0,0,83,82,1,0,0,0,84,85,1,0,0,0,
        85,83,1,0,0,0,85,86,1,0,0,0,86,17,1,0,0,0,87,88,5,9,0,0,88,19,1,
        0,0,0,89,90,7,1,0,0,90,21,1,0,0,0,91,95,5,7,0,0,92,94,5,1,0,0,93,
        92,1,0,0,0,94,97,1,0,0,0,95,93,1,0,0,0,95,96,1,0,0,0,96,98,1,0,0,
        0,97,95,1,0,0,0,98,108,3,16,8,0,99,103,5,8,0,0,100,102,5,1,0,0,101,
        100,1,0,0,0,102,105,1,0,0,0,103,101,1,0,0,0,103,104,1,0,0,0,104,
        106,1,0,0,0,105,103,1,0,0,0,106,108,3,16,8,0,107,91,1,0,0,0,107,
        99,1,0,0,0,108,23,1,0,0,0,15,25,32,36,46,51,56,62,64,70,79,83,85,
        95,103,107
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
                      "UNQUOTED" ]

    RULE_cmdline = 0
    RULE_commands = 1
    RULE_command = 2
    RULE_pipe = 3
    RULE_call = 4
    RULE_cmd = 5
    RULE_subcommand = 6
    RULE_atom = 7
    RULE_argument = 8
    RULE_unquoted = 9
    RULE_quoted = 10
    RULE_redirection = 11

    ruleNames =  [ "cmdline", "commands", "command", "pipe", "call", "cmd", 
                   "subcommand", "atom", "argument", "unquoted", "quoted", 
                   "redirection" ]

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

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
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
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1008) != 0):
                self.state = 24
                self.commands()


            self.state = 27
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
            self.state = 29
            self.command()
            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 30
                self.match(shellParser.SEMICOLON)
                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1008) != 0):
                    self.state = 31
                    self.command()


                self.state = 38
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
            self.state = 39
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
            self.state = 41
            self.call()
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 42
                self.match(shellParser.PIPE)
                self.state = 43
                self.call()
                self.state = 48
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

        def cmd(self):
            return self.getTypedRuleContext(shellParser.CmdContext,0)


        def redirection(self):
            return self.getTypedRuleContext(shellParser.RedirectionContext,0)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(shellParser.WS)
            else:
                return self.getToken(shellParser.WS, i)

        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(shellParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(shellParser.ArgumentContext,i)


        def atom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(shellParser.AtomContext)
            else:
                return self.getTypedRuleContext(shellParser.AtomContext,i)


        def subcommand(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(shellParser.SubcommandContext)
            else:
                return self.getTypedRuleContext(shellParser.SubcommandContext,i)


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
            self.state = 51
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 5, 6, 9]:
                self.state = 49
                self.cmd()
                pass
            elif token in [7, 8]:
                self.state = 50
                self.redirection()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 56
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 53
                    self.match(shellParser.WS) 
                self.state = 58
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1008) != 0):
                self.state = 62
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                if la_ == 1:
                    self.state = 59
                    self.argument()
                    pass

                elif la_ == 2:
                    self.state = 60
                    self.atom()
                    pass

                elif la_ == 3:
                    self.state = 61
                    self.subcommand()
                    pass


                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 67
                self.match(shellParser.WS)
                self.state = 72
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SINGLE_QUOTED(self):
            return self.getToken(shellParser.SINGLE_QUOTED, 0)

        def DOUBLE_QUOTED(self):
            return self.getToken(shellParser.DOUBLE_QUOTED, 0)

        def BACKQUOTED(self):
            return self.getToken(shellParser.BACKQUOTED, 0)

        def UNQUOTED(self):
            return self.getToken(shellParser.UNQUOTED, 0)

        def getRuleIndex(self):
            return shellParser.RULE_cmd

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCmd" ):
                return visitor.visitCmd(self)
            else:
                return visitor.visitChildren(self)




    def cmd(self):

        localctx = shellParser.CmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_cmd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 624) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubcommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BACKQUOTED(self):
            return self.getToken(shellParser.BACKQUOTED, 0)

        def getRuleIndex(self):
            return shellParser.RULE_subcommand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubcommand" ):
                return visitor.visitSubcommand(self)
            else:
                return visitor.visitChildren(self)




    def subcommand(self):

        localctx = shellParser.SubcommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_subcommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(shellParser.BACKQUOTED)
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
        self.enterRule(localctx, 14, self.RULE_atom)
        try:
            self.state = 79
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.redirection()
                pass
            elif token in [4, 5, 6, 9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 78
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


    class ArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def quoted(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(shellParser.QuotedContext)
            else:
                return self.getTypedRuleContext(shellParser.QuotedContext,i)


        def unquoted(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(shellParser.UnquotedContext)
            else:
                return self.getTypedRuleContext(shellParser.UnquotedContext,i)


        def getRuleIndex(self):
            return shellParser.RULE_argument

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument" ):
                return visitor.visitArgument(self)
            else:
                return visitor.visitChildren(self)




    def argument(self):

        localctx = shellParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 83
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [4, 5, 6]:
                        self.state = 81
                        self.quoted()
                        pass
                    elif token in [9]:
                        self.state = 82
                        self.unquoted()
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 85 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

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
            self.state = 87
            self.match(shellParser.UNQUOTED)
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

        def SINGLE_QUOTED(self):
            return self.getToken(shellParser.SINGLE_QUOTED, 0)

        def DOUBLE_QUOTED(self):
            return self.getToken(shellParser.DOUBLE_QUOTED, 0)

        def BACKQUOTED(self):
            return self.getToken(shellParser.BACKQUOTED, 0)

        def getRuleIndex(self):
            return shellParser.RULE_quoted

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuoted" ):
                return visitor.visitQuoted(self)
            else:
                return visitor.visitChildren(self)




    def quoted(self):

        localctx = shellParser.QuotedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_quoted)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 112) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(shellParser.WS)
            else:
                return self.getToken(shellParser.WS, i)

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
        self.enterRule(localctx, 22, self.RULE_redirection)
        self._la = 0 # Token type
        try:
            self.state = 107
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 91
                self.match(shellParser.REDIRECT_INPUT)
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==1:
                    self.state = 92
                    self.match(shellParser.WS)
                    self.state = 97
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 98
                self.argument()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 99
                self.match(shellParser.REDIRECT_OUTPUT)
                self.state = 103
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==1:
                    self.state = 100
                    self.match(shellParser.WS)
                    self.state = 105
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 106
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





