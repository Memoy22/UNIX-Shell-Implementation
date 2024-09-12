// Generated from C:/Users/MemoyMishra/Documents/UCL/prep/Marshall Wace/UNIX-Shell-Implementation/src/parser/shellLexer.g4 by ANTLR 4.13.1
package parser;
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class shellLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		WS=1, PIPE=2, SEMICOLON=3, REDIRECT_INPUT=4, REDIRECT_OUTPUT=5, UNQUOTED=6, 
		SINGLE_QUOTE=7, DOUBLE_QUOTE=8, BACK_QUOTE=9, SQ_START=10, DQ_START=11, 
		BQ_START=12, SQ_CONTENT=13, SQ_END=14, DQ_CONTENT=15, DQ_END=16, BQ_CONTENT=17, 
		BQ_END=18;
	public static final int
		SINGLE_QUOTE_MODE=1, DOUBLE_QUOTE_MODE=2, BACK_QUOTE_MODE=3;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE", "SINGLE_QUOTE_MODE", "DOUBLE_QUOTE_MODE", "BACK_QUOTE_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"WS", "PIPE", "SEMICOLON", "REDIRECT_INPUT", "REDIRECT_OUTPUT", "UNQUOTED", 
			"SINGLE_QUOTE", "DOUBLE_QUOTE", "BACK_QUOTE", "SQ_START", "DQ_START", 
			"BQ_START", "SQ_CONTENT", "SQ_END", "DQ_CONTENT", "DQ_END", "BQ_CONTENT", 
			"BQ_END"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, "'|'", "';'", "'<'", "'>'", null, "'''", "'\"'", "'`'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "WS", "PIPE", "SEMICOLON", "REDIRECT_INPUT", "REDIRECT_OUTPUT", 
			"UNQUOTED", "SINGLE_QUOTE", "DOUBLE_QUOTE", "BACK_QUOTE", "SQ_START", 
			"DQ_START", "BQ_START", "SQ_CONTENT", "SQ_END", "DQ_CONTENT", "DQ_END", 
			"BQ_CONTENT", "BQ_END"
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


	public shellLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "shellLexer.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\u0012i\u0006\uffff\uffff\u0006\uffff\uffff\u0006\uffff\uffff"+
		"\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0001\u0000\u0004\u0000"+
		"*\b\u0000\u000b\u0000\f\u0000+\u0001\u0000\u0001\u0000\u0001\u0001\u0001"+
		"\u0001\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0004\u0001"+
		"\u0004\u0001\u0005\u0004\u00059\b\u0005\u000b\u0005\f\u0005:\u0001\u0006"+
		"\u0001\u0006\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\t\u0001\t\u0001"+
		"\t\u0001\t\u0001\n\u0001\n\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0001\f\u0004\fP\b\f\u000b\f\f\fQ\u0001\r\u0001\r\u0001"+
		"\r\u0001\r\u0001\u000e\u0004\u000eY\b\u000e\u000b\u000e\f\u000eZ\u0001"+
		"\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u0010\u0004\u0010b\b"+
		"\u0010\u000b\u0010\f\u0010c\u0001\u0011\u0001\u0011\u0001\u0011\u0001"+
		"\u0011\u0000\u0000\u0012\u0004\u0001\u0006\u0002\b\u0003\n\u0004\f\u0005"+
		"\u000e\u0006\u0010\u0007\u0012\b\u0014\t\u0016\n\u0018\u000b\u001a\f\u001c"+
		"\r\u001e\u000e \u000f\"\u0010$\u0011&\u0012\u0004\u0000\u0001\u0002\u0003"+
		"\u0005\u0003\u0000\t\n\r\r  \b\u0000\t\n  \"\"\'\';<>>``||\u0002\u0000"+
		"\n\n\'\'\u0002\u0000\n\n\"\"\u0002\u0000\n\n``j\u0000\u0004\u0001\u0000"+
		"\u0000\u0000\u0000\u0006\u0001\u0000\u0000\u0000\u0000\b\u0001\u0000\u0000"+
		"\u0000\u0000\n\u0001\u0000\u0000\u0000\u0000\f\u0001\u0000\u0000\u0000"+
		"\u0000\u000e\u0001\u0000\u0000\u0000\u0000\u0010\u0001\u0000\u0000\u0000"+
		"\u0000\u0012\u0001\u0000\u0000\u0000\u0000\u0014\u0001\u0000\u0000\u0000"+
		"\u0000\u0016\u0001\u0000\u0000\u0000\u0000\u0018\u0001\u0000\u0000\u0000"+
		"\u0000\u001a\u0001\u0000\u0000\u0000\u0001\u001c\u0001\u0000\u0000\u0000"+
		"\u0001\u001e\u0001\u0000\u0000\u0000\u0002 \u0001\u0000\u0000\u0000\u0002"+
		"\"\u0001\u0000\u0000\u0000\u0003$\u0001\u0000\u0000\u0000\u0003&\u0001"+
		"\u0000\u0000\u0000\u0004)\u0001\u0000\u0000\u0000\u0006/\u0001\u0000\u0000"+
		"\u0000\b1\u0001\u0000\u0000\u0000\n3\u0001\u0000\u0000\u0000\f5\u0001"+
		"\u0000\u0000\u0000\u000e8\u0001\u0000\u0000\u0000\u0010<\u0001\u0000\u0000"+
		"\u0000\u0012>\u0001\u0000\u0000\u0000\u0014@\u0001\u0000\u0000\u0000\u0016"+
		"B\u0001\u0000\u0000\u0000\u0018F\u0001\u0000\u0000\u0000\u001aJ\u0001"+
		"\u0000\u0000\u0000\u001cO\u0001\u0000\u0000\u0000\u001eS\u0001\u0000\u0000"+
		"\u0000 X\u0001\u0000\u0000\u0000\"\\\u0001\u0000\u0000\u0000$a\u0001\u0000"+
		"\u0000\u0000&e\u0001\u0000\u0000\u0000(*\u0007\u0000\u0000\u0000)(\u0001"+
		"\u0000\u0000\u0000*+\u0001\u0000\u0000\u0000+)\u0001\u0000\u0000\u0000"+
		"+,\u0001\u0000\u0000\u0000,-\u0001\u0000\u0000\u0000-.\u0006\u0000\u0000"+
		"\u0000.\u0005\u0001\u0000\u0000\u0000/0\u0005|\u0000\u00000\u0007\u0001"+
		"\u0000\u0000\u000012\u0005;\u0000\u00002\t\u0001\u0000\u0000\u000034\u0005"+
		"<\u0000\u00004\u000b\u0001\u0000\u0000\u000056\u0005>\u0000\u00006\r\u0001"+
		"\u0000\u0000\u000079\b\u0001\u0000\u000087\u0001\u0000\u0000\u00009:\u0001"+
		"\u0000\u0000\u0000:8\u0001\u0000\u0000\u0000:;\u0001\u0000\u0000\u0000"+
		";\u000f\u0001\u0000\u0000\u0000<=\u0005\'\u0000\u0000=\u0011\u0001\u0000"+
		"\u0000\u0000>?\u0005\"\u0000\u0000?\u0013\u0001\u0000\u0000\u0000@A\u0005"+
		"`\u0000\u0000A\u0015\u0001\u0000\u0000\u0000BC\u0003\u0010\u0006\u0000"+
		"CD\u0001\u0000\u0000\u0000DE\u0006\t\u0001\u0000E\u0017\u0001\u0000\u0000"+
		"\u0000FG\u0003\u0012\u0007\u0000GH\u0001\u0000\u0000\u0000HI\u0006\n\u0002"+
		"\u0000I\u0019\u0001\u0000\u0000\u0000JK\u0003\u0014\b\u0000KL\u0001\u0000"+
		"\u0000\u0000LM\u0006\u000b\u0003\u0000M\u001b\u0001\u0000\u0000\u0000"+
		"NP\b\u0002\u0000\u0000ON\u0001\u0000\u0000\u0000PQ\u0001\u0000\u0000\u0000"+
		"QO\u0001\u0000\u0000\u0000QR\u0001\u0000\u0000\u0000R\u001d\u0001\u0000"+
		"\u0000\u0000ST\u0003\u0010\u0006\u0000TU\u0001\u0000\u0000\u0000UV\u0006"+
		"\r\u0004\u0000V\u001f\u0001\u0000\u0000\u0000WY\b\u0003\u0000\u0000XW"+
		"\u0001\u0000\u0000\u0000YZ\u0001\u0000\u0000\u0000ZX\u0001\u0000\u0000"+
		"\u0000Z[\u0001\u0000\u0000\u0000[!\u0001\u0000\u0000\u0000\\]\u0003\u0012"+
		"\u0007\u0000]^\u0001\u0000\u0000\u0000^_\u0006\u000f\u0004\u0000_#\u0001"+
		"\u0000\u0000\u0000`b\b\u0004\u0000\u0000a`\u0001\u0000\u0000\u0000bc\u0001"+
		"\u0000\u0000\u0000ca\u0001\u0000\u0000\u0000cd\u0001\u0000\u0000\u0000"+
		"d%\u0001\u0000\u0000\u0000ef\u0003\u0014\b\u0000fg\u0001\u0000\u0000\u0000"+
		"gh\u0006\u0011\u0004\u0000h\'\u0001\u0000\u0000\u0000\t\u0000\u0001\u0002"+
		"\u0003+:QZc\u0005\u0006\u0000\u0000\u0005\u0001\u0000\u0005\u0002\u0000"+
		"\u0005\u0003\u0000\u0004\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}