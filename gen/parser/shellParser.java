// Generated from D:/MEMOY/UCL/prep/Marshall Wace/UNIX-Shell-Implementation/src/parser/shellParser.g4 by ANTLR 4.13.1
package parser;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class shellParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		WS=1, PIPE=2, SEMICOLON=3, REDIRECT_INPUT=4, REDIRECT_OUTPUT=5, UNQUOTED=6, 
		SQ_START=7, DQ_START=8, BQ_START=9, SQ_CONTENT=10, SQ_END=11, DQ_CONTENT=12, 
		BQ_START_IN_DQ=13, DQ_END=14, BQ_CONTENT=15, BQ_END=16;
	public static final int
		RULE_cmdline = 0, RULE_commands = 1, RULE_command = 2, RULE_pipe = 3, 
		RULE_call = 4, RULE_argument = 5, RULE_atom = 6, RULE_redirection = 7, 
		RULE_quoted = 8, RULE_unquoted = 9, RULE_singleQuoted = 10, RULE_doubleQuoted = 11, 
		RULE_content = 12, RULE_backQuotedInDoubleQuoted = 13, RULE_backQuoted = 14;
	private static String[] makeRuleNames() {
		return new String[] {
			"cmdline", "commands", "command", "pipe", "call", "argument", "atom", 
			"redirection", "quoted", "unquoted", "singleQuoted", "doubleQuoted", 
			"content", "backQuotedInDoubleQuoted", "backQuoted"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, "'|'", "';'", "'<'", "'>'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "WS", "PIPE", "SEMICOLON", "REDIRECT_INPUT", "REDIRECT_OUTPUT", 
			"UNQUOTED", "SQ_START", "DQ_START", "BQ_START", "SQ_CONTENT", "SQ_END", 
			"DQ_CONTENT", "BQ_START_IN_DQ", "DQ_END", "BQ_CONTENT", "BQ_END"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "shellParser.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public shellParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CmdlineContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(shellParser.EOF, 0); }
		public CommandsContext commands() {
			return getRuleContext(CommandsContext.class,0);
		}
		public CmdlineContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cmdline; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof shellParserListener ) ((shellParserListener)listener).enterCmdline(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof shellParserListener ) ((shellParserListener)listener).exitCmdline(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof shellParserVisitor ) return ((shellParserVisitor<? extends T>)visitor).visitCmdline(this);
			else return visitor.visitChildren(this);
		}
	}

	public final CmdlineContext cmdline() throws RecognitionException {
		CmdlineContext _localctx = new CmdlineContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_cmdline);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(31);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1008L) != 0)) {
				{
				setState(30);
				commands();
				}
			}

			setState(33);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CommandsContext extends ParserRuleContext {
		public List<CommandContext> command() {
			return getRuleContexts(CommandContext.class);
		}
		public CommandContext command(int i) {
			return getRuleContext(CommandContext.class,i);
		}
		public List<TerminalNode> SEMICOLON() { return getTokens(shellParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(shellParser.SEMICOLON, i);
		}
		public CommandsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_commands; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof shellParserListener ) ((shellParserListener)listener).enterCommands(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof shellParserListener ) ((shellParserListener)listener).exitCommands(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof shellParserVisitor ) return ((shellParserVisitor<? extends T>)visitor).visitCommands(this);
			else return visitor.visitChildren(this);
		}
	}

	public final CommandsContext commands() throws RecognitionException {
		CommandsContext _localctx = new CommandsContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_commands);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(35);
			command();
			setState(40);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==SEMICOLON) {
				{
				{
				setState(36);
				match(SEMICOLON);
				setState(37);
				command();
				}
				}
				setState(42);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CommandContext extends ParserRuleContext {
		public PipeContext pipe() {
			return getRuleContext(PipeContext.class,0);
		}
		public CommandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_command; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof shellParserListener ) ((shellParserListener)listener).enterCommand(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof shellParserListener ) ((shellParserListener)listener).exitCommand(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof shellParserVisitor ) return ((shellParserVisitor<? extends T>)visitor).visitCommand(this);
			else return visitor.visitChildren(this);
		}
	}

	public final CommandContext command() throws RecognitionException {
		CommandContext _localctx = new CommandContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_command);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(43);
			pipe();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PipeContext extends ParserRuleContext {
		public List<CallContext> call() {
			return getRuleContexts(CallContext.class);
		}
		public CallContext call(int i) {
			return getRuleContext(CallContext.class,i);
		}
		public List<TerminalNode> PIPE() { return getTokens(shellParser.PIPE); }
		public TerminalNode PIPE(int i) {
			return getToken(shellParser.PIPE, i);
		}
		public PipeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_pipe; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof shellParserListener ) ((shellParserListener)listener).enterPipe(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof shellParserListener ) ((shellParserListener)listener).exitPipe(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof shellParserVisitor ) return ((shellParserVisitor<? extends T>)visitor).visitPipe(this);
			else return visitor.visitChildren(this);
		}
	}

	public final PipeContext pipe() throws RecognitionException {
		PipeContext _localctx = new PipeContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_pipe);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(45);
			call();
			setState(50);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==PIPE) {
				{
				{
				setState(46);
				match(PIPE);
				setState(47);
				call();
				}
				}
				setState(52);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CallContext extends ParserRuleContext {
		public ArgumentContext argument() {
			return getRuleContext(ArgumentContext.class,0);
		}
		public List<RedirectionContext> redirection() {
			return getRuleContexts(RedirectionContext.class);
		}
		public RedirectionContext redirection(int i) {
			return getRuleContext(RedirectionContext.class,i);
		}
		public List<AtomContext> atom() {
			return getRuleContexts(AtomContext.class);
		}
		public AtomContext atom(int i) {
			return getRuleContext(AtomContext.class,i);
		}
		public CallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_call; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof shellParserListener ) ((shellParserListener)listener).enterCall(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof shellParserListener ) ((shellParserListener)listener).exitCall(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof shellParserVisitor ) return ((shellParserVisitor<? extends T>)visitor).visitCall(this);
			else return visitor.visitChildren(this);
		}
	}

	public final CallContext call() throws RecognitionException {
		CallContext _localctx = new CallContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_call);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(56);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==REDIRECT_INPUT || _la==REDIRECT_OUTPUT) {
				{
				{
				setState(53);
				redirection();
				}
				}
				setState(58);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(59);
			argument();
			setState(63);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1008L) != 0)) {
				{
				{
				setState(60);
				atom();
				}
				}
				setState(65);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ArgumentContext extends ParserRuleContext {
		public QuotedContext quoted() {
			return getRuleContext(QuotedContext.class,0);
		}
		public UnquotedContext unquoted() {
			return getRuleContext(UnquotedContext.class,0);
		}
		public ArgumentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_argument; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof shellParserListener ) ((shellParserListener)listener).enterArgument(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof shellParserListener ) ((shellParserListener)listener).exitArgument(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof shellParserVisitor ) return ((shellParserVisitor<? extends T>)visitor).visitArgument(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ArgumentContext argument() throws RecognitionException {
		ArgumentContext _localctx = new ArgumentContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_argument);
		try {
			setState(68);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case SQ_START:
			case DQ_START:
			case BQ_START:
				enterOuterAlt(_localctx, 1);
				{
				setState(66);
				quoted();
				}
				break;
			case UNQUOTED:
				enterOuterAlt(_localctx, 2);
				{
				setState(67);
				unquoted();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AtomContext extends ParserRuleContext {
		public RedirectionContext redirection() {
			return getRuleContext(RedirectionContext.class,0);
		}
		public ArgumentContext argument() {
			return getRuleContext(ArgumentContext.class,0);
		}
		public AtomContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atom; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof shellParserListener ) ((shellParserListener)listener).enterAtom(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof shellParserListener ) ((shellParserListener)listener).exitAtom(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof shellParserVisitor ) return ((shellParserVisitor<? extends T>)visitor).visitAtom(this);
			else return visitor.visitChildren(this);
		}
	}

	public final AtomContext atom() throws RecognitionException {
		AtomContext _localctx = new AtomContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_atom);
		try {
			setState(72);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case REDIRECT_INPUT:
			case REDIRECT_OUTPUT:
				enterOuterAlt(_localctx, 1);
				{
				setState(70);
				redirection();
				}
				break;
			case UNQUOTED:
			case SQ_START:
			case DQ_START:
			case BQ_START:
				enterOuterAlt(_localctx, 2);
				{
				setState(71);
				argument();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RedirectionContext extends ParserRuleContext {
		public TerminalNode REDIRECT_INPUT() { return getToken(shellParser.REDIRECT_INPUT, 0); }
		public ArgumentContext argument() {
			return getRuleContext(ArgumentContext.class,0);
		}
		public TerminalNode REDIRECT_OUTPUT() { return getToken(shellParser.REDIRECT_OUTPUT, 0); }
		public RedirectionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_redirection; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof shellParserListener ) ((shellParserListener)listener).enterRedirection(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof shellParserListener ) ((shellParserListener)listener).exitRedirection(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof shellParserVisitor ) return ((shellParserVisitor<? extends T>)visitor).visitRedirection(this);
			else return visitor.visitChildren(this);
		}
	}

	public final RedirectionContext redirection() throws RecognitionException {
		RedirectionContext _localctx = new RedirectionContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_redirection);
		try {
			setState(78);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case REDIRECT_INPUT:
				enterOuterAlt(_localctx, 1);
				{
				setState(74);
				match(REDIRECT_INPUT);
				setState(75);
				argument();
				}
				break;
			case REDIRECT_OUTPUT:
				enterOuterAlt(_localctx, 2);
				{
				setState(76);
				match(REDIRECT_OUTPUT);
				setState(77);
				argument();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class QuotedContext extends ParserRuleContext {
		public SingleQuotedContext singleQuoted() {
			return getRuleContext(SingleQuotedContext.class,0);
		}
		public DoubleQuotedContext doubleQuoted() {
			return getRuleContext(DoubleQuotedContext.class,0);
		}
		public BackQuotedContext backQuoted() {
			return getRuleContext(BackQuotedContext.class,0);
		}
		public QuotedContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_quoted; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof shellParserListener ) ((shellParserListener)listener).enterQuoted(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof shellParserListener ) ((shellParserListener)listener).exitQuoted(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof shellParserVisitor ) return ((shellParserVisitor<? extends T>)visitor).visitQuoted(this);
			else return visitor.visitChildren(this);
		}
	}

	public final QuotedContext quoted() throws RecognitionException {
		QuotedContext _localctx = new QuotedContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_quoted);
		try {
			setState(83);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case SQ_START:
				enterOuterAlt(_localctx, 1);
				{
				setState(80);
				singleQuoted();
				}
				break;
			case DQ_START:
				enterOuterAlt(_localctx, 2);
				{
				setState(81);
				doubleQuoted();
				}
				break;
			case BQ_START:
				enterOuterAlt(_localctx, 3);
				{
				setState(82);
				backQuoted();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class UnquotedContext extends ParserRuleContext {
		public TerminalNode UNQUOTED() { return getToken(shellParser.UNQUOTED, 0); }
		public UnquotedContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unquoted; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof shellParserListener ) ((shellParserListener)listener).enterUnquoted(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof shellParserListener ) ((shellParserListener)listener).exitUnquoted(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof shellParserVisitor ) return ((shellParserVisitor<? extends T>)visitor).visitUnquoted(this);
			else return visitor.visitChildren(this);
		}
	}

	public final UnquotedContext unquoted() throws RecognitionException {
		UnquotedContext _localctx = new UnquotedContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_unquoted);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(85);
			match(UNQUOTED);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SingleQuotedContext extends ParserRuleContext {
		public TerminalNode SQ_START() { return getToken(shellParser.SQ_START, 0); }
		public TerminalNode SQ_CONTENT() { return getToken(shellParser.SQ_CONTENT, 0); }
		public TerminalNode SQ_END() { return getToken(shellParser.SQ_END, 0); }
		public SingleQuotedContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_singleQuoted; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof shellParserListener ) ((shellParserListener)listener).enterSingleQuoted(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof shellParserListener ) ((shellParserListener)listener).exitSingleQuoted(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof shellParserVisitor ) return ((shellParserVisitor<? extends T>)visitor).visitSingleQuoted(this);
			else return visitor.visitChildren(this);
		}
	}

	public final SingleQuotedContext singleQuoted() throws RecognitionException {
		SingleQuotedContext _localctx = new SingleQuotedContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_singleQuoted);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(87);
			match(SQ_START);
			setState(88);
			match(SQ_CONTENT);
			setState(89);
			match(SQ_END);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DoubleQuotedContext extends ParserRuleContext {
		public TerminalNode DQ_START() { return getToken(shellParser.DQ_START, 0); }
		public ContentContext content() {
			return getRuleContext(ContentContext.class,0);
		}
		public TerminalNode DQ_END() { return getToken(shellParser.DQ_END, 0); }
		public DoubleQuotedContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_doubleQuoted; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof shellParserListener ) ((shellParserListener)listener).enterDoubleQuoted(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof shellParserListener ) ((shellParserListener)listener).exitDoubleQuoted(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof shellParserVisitor ) return ((shellParserVisitor<? extends T>)visitor).visitDoubleQuoted(this);
			else return visitor.visitChildren(this);
		}
	}

	public final DoubleQuotedContext doubleQuoted() throws RecognitionException {
		DoubleQuotedContext _localctx = new DoubleQuotedContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_doubleQuoted);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(91);
			match(DQ_START);
			setState(92);
			content();
			setState(93);
			match(DQ_END);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ContentContext extends ParserRuleContext {
		public List<TerminalNode> DQ_CONTENT() { return getTokens(shellParser.DQ_CONTENT); }
		public TerminalNode DQ_CONTENT(int i) {
			return getToken(shellParser.DQ_CONTENT, i);
		}
		public List<BackQuotedInDoubleQuotedContext> backQuotedInDoubleQuoted() {
			return getRuleContexts(BackQuotedInDoubleQuotedContext.class);
		}
		public BackQuotedInDoubleQuotedContext backQuotedInDoubleQuoted(int i) {
			return getRuleContext(BackQuotedInDoubleQuotedContext.class,i);
		}
		public ContentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_content; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof shellParserListener ) ((shellParserListener)listener).enterContent(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof shellParserListener ) ((shellParserListener)listener).exitContent(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof shellParserVisitor ) return ((shellParserVisitor<? extends T>)visitor).visitContent(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ContentContext content() throws RecognitionException {
		ContentContext _localctx = new ContentContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_content);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(99);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==DQ_CONTENT || _la==BQ_START_IN_DQ) {
				{
				setState(97);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case DQ_CONTENT:
					{
					setState(95);
					match(DQ_CONTENT);
					}
					break;
				case BQ_START_IN_DQ:
					{
					setState(96);
					backQuotedInDoubleQuoted();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(101);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BackQuotedInDoubleQuotedContext extends ParserRuleContext {
		public TerminalNode BQ_START_IN_DQ() { return getToken(shellParser.BQ_START_IN_DQ, 0); }
		public TerminalNode BQ_CONTENT() { return getToken(shellParser.BQ_CONTENT, 0); }
		public TerminalNode BQ_END() { return getToken(shellParser.BQ_END, 0); }
		public BackQuotedInDoubleQuotedContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_backQuotedInDoubleQuoted; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof shellParserListener ) ((shellParserListener)listener).enterBackQuotedInDoubleQuoted(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof shellParserListener ) ((shellParserListener)listener).exitBackQuotedInDoubleQuoted(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof shellParserVisitor ) return ((shellParserVisitor<? extends T>)visitor).visitBackQuotedInDoubleQuoted(this);
			else return visitor.visitChildren(this);
		}
	}

	public final BackQuotedInDoubleQuotedContext backQuotedInDoubleQuoted() throws RecognitionException {
		BackQuotedInDoubleQuotedContext _localctx = new BackQuotedInDoubleQuotedContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_backQuotedInDoubleQuoted);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(102);
			match(BQ_START_IN_DQ);
			setState(103);
			match(BQ_CONTENT);
			setState(104);
			match(BQ_END);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BackQuotedContext extends ParserRuleContext {
		public TerminalNode BQ_START() { return getToken(shellParser.BQ_START, 0); }
		public TerminalNode BQ_CONTENT() { return getToken(shellParser.BQ_CONTENT, 0); }
		public TerminalNode BQ_END() { return getToken(shellParser.BQ_END, 0); }
		public BackQuotedContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_backQuoted; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof shellParserListener ) ((shellParserListener)listener).enterBackQuoted(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof shellParserListener ) ((shellParserListener)listener).exitBackQuoted(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof shellParserVisitor ) return ((shellParserVisitor<? extends T>)visitor).visitBackQuoted(this);
			else return visitor.visitChildren(this);
		}
	}

	public final BackQuotedContext backQuoted() throws RecognitionException {
		BackQuotedContext _localctx = new BackQuotedContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_backQuoted);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(106);
			match(BQ_START);
			setState(107);
			match(BQ_CONTENT);
			setState(108);
			match(BQ_END);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u0010o\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0001\u0000\u0003\u0000"+
		" \b\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0005\u0001\'\b\u0001\n\u0001\f\u0001*\t\u0001\u0001\u0002\u0001\u0002"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0005\u00031\b\u0003\n\u0003\f\u0003"+
		"4\t\u0003\u0001\u0004\u0005\u00047\b\u0004\n\u0004\f\u0004:\t\u0004\u0001"+
		"\u0004\u0001\u0004\u0005\u0004>\b\u0004\n\u0004\f\u0004A\t\u0004\u0001"+
		"\u0005\u0001\u0005\u0003\u0005E\b\u0005\u0001\u0006\u0001\u0006\u0003"+
		"\u0006I\b\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0003"+
		"\u0007O\b\u0007\u0001\b\u0001\b\u0001\b\u0003\bT\b\b\u0001\t\u0001\t\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0001\f\u0001\f\u0005\fb\b\f\n\f\f\fe\t\f\u0001\r\u0001\r\u0001\r\u0001"+
		"\r\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0000\u0000"+
		"\u000f\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018"+
		"\u001a\u001c\u0000\u0000k\u0000\u001f\u0001\u0000\u0000\u0000\u0002#\u0001"+
		"\u0000\u0000\u0000\u0004+\u0001\u0000\u0000\u0000\u0006-\u0001\u0000\u0000"+
		"\u0000\b8\u0001\u0000\u0000\u0000\nD\u0001\u0000\u0000\u0000\fH\u0001"+
		"\u0000\u0000\u0000\u000eN\u0001\u0000\u0000\u0000\u0010S\u0001\u0000\u0000"+
		"\u0000\u0012U\u0001\u0000\u0000\u0000\u0014W\u0001\u0000\u0000\u0000\u0016"+
		"[\u0001\u0000\u0000\u0000\u0018c\u0001\u0000\u0000\u0000\u001af\u0001"+
		"\u0000\u0000\u0000\u001cj\u0001\u0000\u0000\u0000\u001e \u0003\u0002\u0001"+
		"\u0000\u001f\u001e\u0001\u0000\u0000\u0000\u001f \u0001\u0000\u0000\u0000"+
		" !\u0001\u0000\u0000\u0000!\"\u0005\u0000\u0000\u0001\"\u0001\u0001\u0000"+
		"\u0000\u0000#(\u0003\u0004\u0002\u0000$%\u0005\u0003\u0000\u0000%\'\u0003"+
		"\u0004\u0002\u0000&$\u0001\u0000\u0000\u0000\'*\u0001\u0000\u0000\u0000"+
		"(&\u0001\u0000\u0000\u0000()\u0001\u0000\u0000\u0000)\u0003\u0001\u0000"+
		"\u0000\u0000*(\u0001\u0000\u0000\u0000+,\u0003\u0006\u0003\u0000,\u0005"+
		"\u0001\u0000\u0000\u0000-2\u0003\b\u0004\u0000./\u0005\u0002\u0000\u0000"+
		"/1\u0003\b\u0004\u00000.\u0001\u0000\u0000\u000014\u0001\u0000\u0000\u0000"+
		"20\u0001\u0000\u0000\u000023\u0001\u0000\u0000\u00003\u0007\u0001\u0000"+
		"\u0000\u000042\u0001\u0000\u0000\u000057\u0003\u000e\u0007\u000065\u0001"+
		"\u0000\u0000\u00007:\u0001\u0000\u0000\u000086\u0001\u0000\u0000\u0000"+
		"89\u0001\u0000\u0000\u00009;\u0001\u0000\u0000\u0000:8\u0001\u0000\u0000"+
		"\u0000;?\u0003\n\u0005\u0000<>\u0003\f\u0006\u0000=<\u0001\u0000\u0000"+
		"\u0000>A\u0001\u0000\u0000\u0000?=\u0001\u0000\u0000\u0000?@\u0001\u0000"+
		"\u0000\u0000@\t\u0001\u0000\u0000\u0000A?\u0001\u0000\u0000\u0000BE\u0003"+
		"\u0010\b\u0000CE\u0003\u0012\t\u0000DB\u0001\u0000\u0000\u0000DC\u0001"+
		"\u0000\u0000\u0000E\u000b\u0001\u0000\u0000\u0000FI\u0003\u000e\u0007"+
		"\u0000GI\u0003\n\u0005\u0000HF\u0001\u0000\u0000\u0000HG\u0001\u0000\u0000"+
		"\u0000I\r\u0001\u0000\u0000\u0000JK\u0005\u0004\u0000\u0000KO\u0003\n"+
		"\u0005\u0000LM\u0005\u0005\u0000\u0000MO\u0003\n\u0005\u0000NJ\u0001\u0000"+
		"\u0000\u0000NL\u0001\u0000\u0000\u0000O\u000f\u0001\u0000\u0000\u0000"+
		"PT\u0003\u0014\n\u0000QT\u0003\u0016\u000b\u0000RT\u0003\u001c\u000e\u0000"+
		"SP\u0001\u0000\u0000\u0000SQ\u0001\u0000\u0000\u0000SR\u0001\u0000\u0000"+
		"\u0000T\u0011\u0001\u0000\u0000\u0000UV\u0005\u0006\u0000\u0000V\u0013"+
		"\u0001\u0000\u0000\u0000WX\u0005\u0007\u0000\u0000XY\u0005\n\u0000\u0000"+
		"YZ\u0005\u000b\u0000\u0000Z\u0015\u0001\u0000\u0000\u0000[\\\u0005\b\u0000"+
		"\u0000\\]\u0003\u0018\f\u0000]^\u0005\u000e\u0000\u0000^\u0017\u0001\u0000"+
		"\u0000\u0000_b\u0005\f\u0000\u0000`b\u0003\u001a\r\u0000a_\u0001\u0000"+
		"\u0000\u0000a`\u0001\u0000\u0000\u0000be\u0001\u0000\u0000\u0000ca\u0001"+
		"\u0000\u0000\u0000cd\u0001\u0000\u0000\u0000d\u0019\u0001\u0000\u0000"+
		"\u0000ec\u0001\u0000\u0000\u0000fg\u0005\r\u0000\u0000gh\u0005\u000f\u0000"+
		"\u0000hi\u0005\u0010\u0000\u0000i\u001b\u0001\u0000\u0000\u0000jk\u0005"+
		"\t\u0000\u0000kl\u0005\u000f\u0000\u0000lm\u0005\u0010\u0000\u0000m\u001d"+
		"\u0001\u0000\u0000\u0000\u000b\u001f(28?DHNSac";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}