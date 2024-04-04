// Generated from C:/Users/MemoyMishra/Documents/UCL/year2_2023/softwareEngineering_COMP0010/comp0010-shell-python-p26/src/shellParser.g4 by ANTLR 4.13.1
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
		WS=1, PIPE=2, SEMICOLON=3, SINGLE_QUOTED=4, DOUBLE_QUOTED=5, BACKQUOTED=6, 
		REDIRECT_INPUT=7, REDIRECT_OUTPUT=8, CMD=9, UNQUOTED=10;
	public static final int
		RULE_cmdline = 0, RULE_commands = 1, RULE_command = 2, RULE_pipe = 3, 
		RULE_call = 4, RULE_cmd = 5, RULE_subcommand = 6, RULE_atom = 7, RULE_argument = 8, 
		RULE_unquoted = 9, RULE_quoted = 10, RULE_redirection = 11;
	private static String[] makeRuleNames() {
		return new String[] {
			"cmdline", "commands", "command", "pipe", "call", "cmd", "subcommand", 
			"atom", "argument", "unquoted", "quoted", "redirection"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, "'|'", "';'", null, null, null, "'<'", "'>'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "WS", "PIPE", "SEMICOLON", "SINGLE_QUOTED", "DOUBLE_QUOTED", "BACKQUOTED", 
			"REDIRECT_INPUT", "REDIRECT_OUTPUT", "CMD", "UNQUOTED"
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
			setState(25);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1472L) != 0)) {
				{
				setState(24);
				commands();
				}
			}

			setState(27);
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
			setState(29);
			command();
			setState(34);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==SEMICOLON) {
				{
				{
				setState(30);
				match(SEMICOLON);
				setState(31);
				command();
				}
				}
				setState(36);
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
			setState(37);
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
			setState(39);
			call();
			setState(44);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==PIPE) {
				{
				{
				setState(40);
				match(PIPE);
				setState(41);
				call();
				}
				}
				setState(46);
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
		public CmdContext cmd() {
			return getRuleContext(CmdContext.class,0);
		}
		public List<TerminalNode> WS() { return getTokens(shellParser.WS); }
		public TerminalNode WS(int i) {
			return getToken(shellParser.WS, i);
		}
		public List<ArgumentContext> argument() {
			return getRuleContexts(ArgumentContext.class);
		}
		public ArgumentContext argument(int i) {
			return getRuleContext(ArgumentContext.class,i);
		}
		public List<AtomContext> atom() {
			return getRuleContexts(AtomContext.class);
		}
		public AtomContext atom(int i) {
			return getRuleContext(AtomContext.class,i);
		}
		public List<SubcommandContext> subcommand() {
			return getRuleContexts(SubcommandContext.class);
		}
		public SubcommandContext subcommand(int i) {
			return getRuleContext(SubcommandContext.class,i);
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
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(47);
			cmd();
			setState(51);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(48);
					match(WS);
					}
					} 
				}
				setState(53);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
			}
			setState(59);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					setState(57);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
					case 1:
						{
						setState(54);
						argument();
						}
						break;
					case 2:
						{
						setState(55);
						atom();
						}
						break;
					case 3:
						{
						setState(56);
						subcommand();
						}
						break;
					}
					} 
				}
				setState(61);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			}
			setState(65);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==WS) {
				{
				{
				setState(62);
				match(WS);
				}
				}
				setState(67);
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
	public static class CmdContext extends ParserRuleContext {
		public TerminalNode UNQUOTED() { return getToken(shellParser.UNQUOTED, 0); }
		public RedirectionContext redirection() {
			return getRuleContext(RedirectionContext.class,0);
		}
		public TerminalNode BACKQUOTED() { return getToken(shellParser.BACKQUOTED, 0); }
		public CmdContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cmd; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof shellParserListener ) ((shellParserListener)listener).enterCmd(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof shellParserListener ) ((shellParserListener)listener).exitCmd(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof shellParserVisitor ) return ((shellParserVisitor<? extends T>)visitor).visitCmd(this);
			else return visitor.visitChildren(this);
		}
	}

	public final CmdContext cmd() throws RecognitionException {
		CmdContext _localctx = new CmdContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_cmd);
		try {
			setState(71);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case UNQUOTED:
				enterOuterAlt(_localctx, 1);
				{
				setState(68);
				match(UNQUOTED);
				}
				break;
			case REDIRECT_INPUT:
			case REDIRECT_OUTPUT:
				enterOuterAlt(_localctx, 2);
				{
				setState(69);
				redirection();
				}
				break;
			case BACKQUOTED:
				enterOuterAlt(_localctx, 3);
				{
				setState(70);
				match(BACKQUOTED);
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
	public static class SubcommandContext extends ParserRuleContext {
		public List<TerminalNode> BACKQUOTED() { return getTokens(shellParser.BACKQUOTED); }
		public TerminalNode BACKQUOTED(int i) {
			return getToken(shellParser.BACKQUOTED, i);
		}
		public CommandsContext commands() {
			return getRuleContext(CommandsContext.class,0);
		}
		public SubcommandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_subcommand; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof shellParserListener ) ((shellParserListener)listener).enterSubcommand(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof shellParserListener ) ((shellParserListener)listener).exitSubcommand(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof shellParserVisitor ) return ((shellParserVisitor<? extends T>)visitor).visitSubcommand(this);
			else return visitor.visitChildren(this);
		}
	}

	public final SubcommandContext subcommand() throws RecognitionException {
		SubcommandContext _localctx = new SubcommandContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_subcommand);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(73);
			match(BACKQUOTED);
			setState(74);
			commands();
			setState(75);
			match(BACKQUOTED);
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
		enterRule(_localctx, 14, RULE_atom);
		try {
			setState(79);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case REDIRECT_INPUT:
			case REDIRECT_OUTPUT:
				enterOuterAlt(_localctx, 1);
				{
				setState(77);
				redirection();
				}
				break;
			case SINGLE_QUOTED:
			case DOUBLE_QUOTED:
			case BACKQUOTED:
			case UNQUOTED:
				enterOuterAlt(_localctx, 2);
				{
				setState(78);
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
	public static class ArgumentContext extends ParserRuleContext {
		public List<QuotedContext> quoted() {
			return getRuleContexts(QuotedContext.class);
		}
		public QuotedContext quoted(int i) {
			return getRuleContext(QuotedContext.class,i);
		}
		public List<UnquotedContext> unquoted() {
			return getRuleContexts(UnquotedContext.class);
		}
		public UnquotedContext unquoted(int i) {
			return getRuleContext(UnquotedContext.class,i);
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
		enterRule(_localctx, 16, RULE_argument);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(83); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					setState(83);
					_errHandler.sync(this);
					switch (_input.LA(1)) {
					case SINGLE_QUOTED:
					case DOUBLE_QUOTED:
					case BACKQUOTED:
						{
						setState(81);
						quoted();
						}
						break;
					case UNQUOTED:
						{
						setState(82);
						unquoted();
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(85); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,10,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
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
			setState(87);
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
	public static class QuotedContext extends ParserRuleContext {
		public TerminalNode SINGLE_QUOTED() { return getToken(shellParser.SINGLE_QUOTED, 0); }
		public TerminalNode DOUBLE_QUOTED() { return getToken(shellParser.DOUBLE_QUOTED, 0); }
		public TerminalNode BACKQUOTED() { return getToken(shellParser.BACKQUOTED, 0); }
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
		enterRule(_localctx, 20, RULE_quoted);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(89);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 112L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
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
	public static class RedirectionContext extends ParserRuleContext {
		public TerminalNode REDIRECT_INPUT() { return getToken(shellParser.REDIRECT_INPUT, 0); }
		public ArgumentContext argument() {
			return getRuleContext(ArgumentContext.class,0);
		}
		public List<TerminalNode> WS() { return getTokens(shellParser.WS); }
		public TerminalNode WS(int i) {
			return getToken(shellParser.WS, i);
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
		enterRule(_localctx, 22, RULE_redirection);
		int _la;
		try {
			setState(107);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case REDIRECT_INPUT:
				enterOuterAlt(_localctx, 1);
				{
				setState(91);
				match(REDIRECT_INPUT);
				setState(95);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==WS) {
					{
					{
					setState(92);
					match(WS);
					}
					}
					setState(97);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(98);
				argument();
				}
				break;
			case REDIRECT_OUTPUT:
				enterOuterAlt(_localctx, 2);
				{
				setState(99);
				match(REDIRECT_OUTPUT);
				setState(103);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==WS) {
					{
					{
					setState(100);
					match(WS);
					}
					}
					setState(105);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(106);
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

	public static final String _serializedATN =
		"\u0004\u0001\nn\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0001"+
		"\u0000\u0003\u0000\u001a\b\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0005\u0001!\b\u0001\n\u0001\f\u0001$\t\u0001\u0001"+
		"\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0005\u0003+\b"+
		"\u0003\n\u0003\f\u0003.\t\u0003\u0001\u0004\u0001\u0004\u0005\u00042\b"+
		"\u0004\n\u0004\f\u00045\t\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0005"+
		"\u0004:\b\u0004\n\u0004\f\u0004=\t\u0004\u0001\u0004\u0005\u0004@\b\u0004"+
		"\n\u0004\f\u0004C\t\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0003\u0005"+
		"H\b\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007"+
		"\u0001\u0007\u0003\u0007P\b\u0007\u0001\b\u0001\b\u0004\bT\b\b\u000b\b"+
		"\f\bU\u0001\t\u0001\t\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0005\u000b"+
		"^\b\u000b\n\u000b\f\u000ba\t\u000b\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0005\u000bf\b\u000b\n\u000b\f\u000bi\t\u000b\u0001\u000b\u0003\u000b"+
		"l\b\u000b\u0001\u000b\u0000\u0000\f\u0000\u0002\u0004\u0006\b\n\f\u000e"+
		"\u0010\u0012\u0014\u0016\u0000\u0001\u0001\u0000\u0004\u0006q\u0000\u0019"+
		"\u0001\u0000\u0000\u0000\u0002\u001d\u0001\u0000\u0000\u0000\u0004%\u0001"+
		"\u0000\u0000\u0000\u0006\'\u0001\u0000\u0000\u0000\b/\u0001\u0000\u0000"+
		"\u0000\nG\u0001\u0000\u0000\u0000\fI\u0001\u0000\u0000\u0000\u000eO\u0001"+
		"\u0000\u0000\u0000\u0010S\u0001\u0000\u0000\u0000\u0012W\u0001\u0000\u0000"+
		"\u0000\u0014Y\u0001\u0000\u0000\u0000\u0016k\u0001\u0000\u0000\u0000\u0018"+
		"\u001a\u0003\u0002\u0001\u0000\u0019\u0018\u0001\u0000\u0000\u0000\u0019"+
		"\u001a\u0001\u0000\u0000\u0000\u001a\u001b\u0001\u0000\u0000\u0000\u001b"+
		"\u001c\u0005\u0000\u0000\u0001\u001c\u0001\u0001\u0000\u0000\u0000\u001d"+
		"\"\u0003\u0004\u0002\u0000\u001e\u001f\u0005\u0003\u0000\u0000\u001f!"+
		"\u0003\u0004\u0002\u0000 \u001e\u0001\u0000\u0000\u0000!$\u0001\u0000"+
		"\u0000\u0000\" \u0001\u0000\u0000\u0000\"#\u0001\u0000\u0000\u0000#\u0003"+
		"\u0001\u0000\u0000\u0000$\"\u0001\u0000\u0000\u0000%&\u0003\u0006\u0003"+
		"\u0000&\u0005\u0001\u0000\u0000\u0000\',\u0003\b\u0004\u0000()\u0005\u0002"+
		"\u0000\u0000)+\u0003\b\u0004\u0000*(\u0001\u0000\u0000\u0000+.\u0001\u0000"+
		"\u0000\u0000,*\u0001\u0000\u0000\u0000,-\u0001\u0000\u0000\u0000-\u0007"+
		"\u0001\u0000\u0000\u0000.,\u0001\u0000\u0000\u0000/3\u0003\n\u0005\u0000"+
		"02\u0005\u0001\u0000\u000010\u0001\u0000\u0000\u000025\u0001\u0000\u0000"+
		"\u000031\u0001\u0000\u0000\u000034\u0001\u0000\u0000\u00004;\u0001\u0000"+
		"\u0000\u000053\u0001\u0000\u0000\u00006:\u0003\u0010\b\u00007:\u0003\u000e"+
		"\u0007\u00008:\u0003\f\u0006\u000096\u0001\u0000\u0000\u000097\u0001\u0000"+
		"\u0000\u000098\u0001\u0000\u0000\u0000:=\u0001\u0000\u0000\u0000;9\u0001"+
		"\u0000\u0000\u0000;<\u0001\u0000\u0000\u0000<A\u0001\u0000\u0000\u0000"+
		"=;\u0001\u0000\u0000\u0000>@\u0005\u0001\u0000\u0000?>\u0001\u0000\u0000"+
		"\u0000@C\u0001\u0000\u0000\u0000A?\u0001\u0000\u0000\u0000AB\u0001\u0000"+
		"\u0000\u0000B\t\u0001\u0000\u0000\u0000CA\u0001\u0000\u0000\u0000DH\u0005"+
		"\n\u0000\u0000EH\u0003\u0016\u000b\u0000FH\u0005\u0006\u0000\u0000GD\u0001"+
		"\u0000\u0000\u0000GE\u0001\u0000\u0000\u0000GF\u0001\u0000\u0000\u0000"+
		"H\u000b\u0001\u0000\u0000\u0000IJ\u0005\u0006\u0000\u0000JK\u0003\u0002"+
		"\u0001\u0000KL\u0005\u0006\u0000\u0000L\r\u0001\u0000\u0000\u0000MP\u0003"+
		"\u0016\u000b\u0000NP\u0003\u0010\b\u0000OM\u0001\u0000\u0000\u0000ON\u0001"+
		"\u0000\u0000\u0000P\u000f\u0001\u0000\u0000\u0000QT\u0003\u0014\n\u0000"+
		"RT\u0003\u0012\t\u0000SQ\u0001\u0000\u0000\u0000SR\u0001\u0000\u0000\u0000"+
		"TU\u0001\u0000\u0000\u0000US\u0001\u0000\u0000\u0000UV\u0001\u0000\u0000"+
		"\u0000V\u0011\u0001\u0000\u0000\u0000WX\u0005\n\u0000\u0000X\u0013\u0001"+
		"\u0000\u0000\u0000YZ\u0007\u0000\u0000\u0000Z\u0015\u0001\u0000\u0000"+
		"\u0000[_\u0005\u0007\u0000\u0000\\^\u0005\u0001\u0000\u0000]\\\u0001\u0000"+
		"\u0000\u0000^a\u0001\u0000\u0000\u0000_]\u0001\u0000\u0000\u0000_`\u0001"+
		"\u0000\u0000\u0000`b\u0001\u0000\u0000\u0000a_\u0001\u0000\u0000\u0000"+
		"bl\u0003\u0010\b\u0000cg\u0005\b\u0000\u0000df\u0005\u0001\u0000\u0000"+
		"ed\u0001\u0000\u0000\u0000fi\u0001\u0000\u0000\u0000ge\u0001\u0000\u0000"+
		"\u0000gh\u0001\u0000\u0000\u0000hj\u0001\u0000\u0000\u0000ig\u0001\u0000"+
		"\u0000\u0000jl\u0003\u0010\b\u0000k[\u0001\u0000\u0000\u0000kc\u0001\u0000"+
		"\u0000\u0000l\u0017\u0001\u0000\u0000\u0000\u000e\u0019\",39;AGOSU_gk";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}