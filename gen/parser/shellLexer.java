// Generated from C:/Users/MemoyMishra/Documents/UCL/year2_2023/softwareEngineering_COMP0010/comp0010-shell-python-p26/src/parser/shellLexer.g4 by ANTLR 4.13.1
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
		WS=1, PIPE=2, SEMICOLON=3, SINGLE_QUOTED=4, DOUBLE_QUOTED=5, BACKQUOTED=6, 
		REDIRECT_INPUT=7, REDIRECT_OUTPUT=8, UNQUOTED=9;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"WS", "PIPE", "SEMICOLON", "SINGLE_QUOTED", "DOUBLE_QUOTED", "BACKQUOTED", 
			"REDIRECT_INPUT", "REDIRECT_OUTPUT", "UNQUOTED", "BACKSLASH", "LETTER", 
			"UNSAFE"
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
			"REDIRECT_INPUT", "REDIRECT_OUTPUT", "UNQUOTED"
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
		"\u0004\u0000\tR\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0001\u0000\u0004\u0000\u001b\b\u0000\u000b\u0000\f\u0000"+
		"\u001c\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0002\u0001"+
		"\u0002\u0001\u0003\u0001\u0003\u0005\u0003\'\b\u0003\n\u0003\f\u0003*"+
		"\t\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0005\u00042\b\u0004\n\u0004\f\u00045\t\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0005\u0005=\b"+
		"\u0005\n\u0005\f\u0005@\t\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001"+
		"\u0006\u0001\u0007\u0001\u0007\u0001\b\u0004\bI\b\b\u000b\b\f\bJ\u0001"+
		"\t\u0001\t\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0000\u0000\f\u0001"+
		"\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007"+
		"\u000f\b\u0011\t\u0013\u0000\u0015\u0000\u0017\u0000\u0001\u0000\u0006"+
		"\u0003\u0000\t\n\r\r  \u0002\u0000\n\n\'\'\u0003\u0000\n\n\"\"``\u0002"+
		"\u0000\n\n``\u0006\u0000\t\n  ;<>>``||\u0002\u0000AZazU\u0000\u0001\u0001"+
		"\u0000\u0000\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005\u0001"+
		"\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000"+
		"\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000"+
		"\u0000\u0000\u000f\u0001\u0000\u0000\u0000\u0000\u0011\u0001\u0000\u0000"+
		"\u0000\u0001\u001a\u0001\u0000\u0000\u0000\u0003 \u0001\u0000\u0000\u0000"+
		"\u0005\"\u0001\u0000\u0000\u0000\u0007$\u0001\u0000\u0000\u0000\t-\u0001"+
		"\u0000\u0000\u0000\u000b8\u0001\u0000\u0000\u0000\rC\u0001\u0000\u0000"+
		"\u0000\u000fE\u0001\u0000\u0000\u0000\u0011H\u0001\u0000\u0000\u0000\u0013"+
		"L\u0001\u0000\u0000\u0000\u0015N\u0001\u0000\u0000\u0000\u0017P\u0001"+
		"\u0000\u0000\u0000\u0019\u001b\u0007\u0000\u0000\u0000\u001a\u0019\u0001"+
		"\u0000\u0000\u0000\u001b\u001c\u0001\u0000\u0000\u0000\u001c\u001a\u0001"+
		"\u0000\u0000\u0000\u001c\u001d\u0001\u0000\u0000\u0000\u001d\u001e\u0001"+
		"\u0000\u0000\u0000\u001e\u001f\u0006\u0000\u0000\u0000\u001f\u0002\u0001"+
		"\u0000\u0000\u0000 !\u0005|\u0000\u0000!\u0004\u0001\u0000\u0000\u0000"+
		"\"#\u0005;\u0000\u0000#\u0006\u0001\u0000\u0000\u0000$(\u0005\'\u0000"+
		"\u0000%\'\b\u0001\u0000\u0000&%\u0001\u0000\u0000\u0000\'*\u0001\u0000"+
		"\u0000\u0000(&\u0001\u0000\u0000\u0000()\u0001\u0000\u0000\u0000)+\u0001"+
		"\u0000\u0000\u0000*(\u0001\u0000\u0000\u0000+,\u0005\'\u0000\u0000,\b"+
		"\u0001\u0000\u0000\u0000-3\u0005\"\u0000\u0000.2\b\u0002\u0000\u0000/"+
		"0\u0005\\\u0000\u000002\t\u0000\u0000\u00001.\u0001\u0000\u0000\u0000"+
		"1/\u0001\u0000\u0000\u000025\u0001\u0000\u0000\u000031\u0001\u0000\u0000"+
		"\u000034\u0001\u0000\u0000\u000046\u0001\u0000\u0000\u000053\u0001\u0000"+
		"\u0000\u000067\u0005\"\u0000\u00007\n\u0001\u0000\u0000\u00008>\u0005"+
		"`\u0000\u00009=\b\u0003\u0000\u0000:;\u0005\\\u0000\u0000;=\t\u0000\u0000"+
		"\u0000<9\u0001\u0000\u0000\u0000<:\u0001\u0000\u0000\u0000=@\u0001\u0000"+
		"\u0000\u0000><\u0001\u0000\u0000\u0000>?\u0001\u0000\u0000\u0000?A\u0001"+
		"\u0000\u0000\u0000@>\u0001\u0000\u0000\u0000AB\u0005`\u0000\u0000B\f\u0001"+
		"\u0000\u0000\u0000CD\u0005<\u0000\u0000D\u000e\u0001\u0000\u0000\u0000"+
		"EF\u0005>\u0000\u0000F\u0010\u0001\u0000\u0000\u0000GI\b\u0004\u0000\u0000"+
		"HG\u0001\u0000\u0000\u0000IJ\u0001\u0000\u0000\u0000JH\u0001\u0000\u0000"+
		"\u0000JK\u0001\u0000\u0000\u0000K\u0012\u0001\u0000\u0000\u0000LM\u0005"+
		"\\\u0000\u0000M\u0014\u0001\u0000\u0000\u0000NO\u0007\u0005\u0000\u0000"+
		"O\u0016\u0001\u0000\u0000\u0000PQ\u0005_\u0000\u0000Q\u0018\u0001\u0000"+
		"\u0000\u0000\b\u0000\u001c(13<>J\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}