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
		SQ_START=7, DQ_START=8, BQ_START=9, SQ_CONTENT=10, SQ_END=11, DQ_CONTENT=12, 
		BQ_START_IN_DQ=13, DQ_END=14, BQ_CONTENT=15, BQ_END=16;
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
			"SINGLE_QUOTE", "DOUBLE_QUOTE", "BACK_QUOTE", "WS", "PIPE", "SEMICOLON", 
			"REDIRECT_INPUT", "REDIRECT_OUTPUT", "UNQUOTED", "SQ_START", "DQ_START", 
			"BQ_START", "SQ_CONTENT", "SQ_END", "DQ_CONTENT", "BQ_START_IN_DQ", "DQ_END", 
			"BQ_CONTENT", "BQ_END"
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
		"\u0004\u0000\u0010o\u0006\uffff\uffff\u0006\uffff\uffff\u0006\uffff\uffff"+
		"\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002"+
		"\u0001\u0003\u0004\u00032\b\u0003\u000b\u0003\f\u00033\u0001\u0003\u0001"+
		"\u0003\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0006\u0001"+
		"\u0006\u0001\u0007\u0001\u0007\u0001\b\u0004\bA\b\b\u000b\b\f\bB\u0001"+
		"\t\u0001\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001\n\u0001\n\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0001\u000b\u0001\f\u0004\fR\b\f\u000b\f\f\f"+
		"S\u0001\r\u0001\r\u0001\r\u0001\r\u0001\u000e\u0004\u000e[\b\u000e\u000b"+
		"\u000e\f\u000e\\\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001"+
		"\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0011\u0004\u0011h\b"+
		"\u0011\u000b\u0011\f\u0011i\u0001\u0012\u0001\u0012\u0001\u0012\u0001"+
		"\u0012\u0000\u0000\u0013\u0004\u0000\u0006\u0000\b\u0000\n\u0001\f\u0002"+
		"\u000e\u0003\u0010\u0004\u0012\u0005\u0014\u0006\u0016\u0007\u0018\b\u001a"+
		"\t\u001c\n\u001e\u000b \f\"\r$\u000e&\u000f(\u0010\u0004\u0000\u0001\u0002"+
		"\u0003\u0005\u0002\u0000\t\n  \b\u0000\t\n  \"\"\'\';<>>``||\u0002\u0000"+
		"\n\n\'\'\u0003\u0000\n\n\"\"``\u0002\u0000\n\n``m\u0000\n\u0001\u0000"+
		"\u0000\u0000\u0000\f\u0001\u0000\u0000\u0000\u0000\u000e\u0001\u0000\u0000"+
		"\u0000\u0000\u0010\u0001\u0000\u0000\u0000\u0000\u0012\u0001\u0000\u0000"+
		"\u0000\u0000\u0014\u0001\u0000\u0000\u0000\u0000\u0016\u0001\u0000\u0000"+
		"\u0000\u0000\u0018\u0001\u0000\u0000\u0000\u0000\u001a\u0001\u0000\u0000"+
		"\u0000\u0001\u001c\u0001\u0000\u0000\u0000\u0001\u001e\u0001\u0000\u0000"+
		"\u0000\u0002 \u0001\u0000\u0000\u0000\u0002\"\u0001\u0000\u0000\u0000"+
		"\u0002$\u0001\u0000\u0000\u0000\u0003&\u0001\u0000\u0000\u0000\u0003("+
		"\u0001\u0000\u0000\u0000\u0004*\u0001\u0000\u0000\u0000\u0006,\u0001\u0000"+
		"\u0000\u0000\b.\u0001\u0000\u0000\u0000\n1\u0001\u0000\u0000\u0000\f7"+
		"\u0001\u0000\u0000\u0000\u000e9\u0001\u0000\u0000\u0000\u0010;\u0001\u0000"+
		"\u0000\u0000\u0012=\u0001\u0000\u0000\u0000\u0014@\u0001\u0000\u0000\u0000"+
		"\u0016D\u0001\u0000\u0000\u0000\u0018H\u0001\u0000\u0000\u0000\u001aL"+
		"\u0001\u0000\u0000\u0000\u001cQ\u0001\u0000\u0000\u0000\u001eU\u0001\u0000"+
		"\u0000\u0000 Z\u0001\u0000\u0000\u0000\"^\u0001\u0000\u0000\u0000$b\u0001"+
		"\u0000\u0000\u0000&g\u0001\u0000\u0000\u0000(k\u0001\u0000\u0000\u0000"+
		"*+\u0005\'\u0000\u0000+\u0005\u0001\u0000\u0000\u0000,-\u0005\"\u0000"+
		"\u0000-\u0007\u0001\u0000\u0000\u0000./\u0005`\u0000\u0000/\t\u0001\u0000"+
		"\u0000\u000002\u0007\u0000\u0000\u000010\u0001\u0000\u0000\u000023\u0001"+
		"\u0000\u0000\u000031\u0001\u0000\u0000\u000034\u0001\u0000\u0000\u0000"+
		"45\u0001\u0000\u0000\u000056\u0006\u0003\u0000\u00006\u000b\u0001\u0000"+
		"\u0000\u000078\u0005|\u0000\u00008\r\u0001\u0000\u0000\u00009:\u0005;"+
		"\u0000\u0000:\u000f\u0001\u0000\u0000\u0000;<\u0005<\u0000\u0000<\u0011"+
		"\u0001\u0000\u0000\u0000=>\u0005>\u0000\u0000>\u0013\u0001\u0000\u0000"+
		"\u0000?A\b\u0001\u0000\u0000@?\u0001\u0000\u0000\u0000AB\u0001\u0000\u0000"+
		"\u0000B@\u0001\u0000\u0000\u0000BC\u0001\u0000\u0000\u0000C\u0015\u0001"+
		"\u0000\u0000\u0000DE\u0003\u0004\u0000\u0000EF\u0001\u0000\u0000\u0000"+
		"FG\u0006\t\u0001\u0000G\u0017\u0001\u0000\u0000\u0000HI\u0003\u0006\u0001"+
		"\u0000IJ\u0001\u0000\u0000\u0000JK\u0006\n\u0002\u0000K\u0019\u0001\u0000"+
		"\u0000\u0000LM\u0003\b\u0002\u0000MN\u0001\u0000\u0000\u0000NO\u0006\u000b"+
		"\u0003\u0000O\u001b\u0001\u0000\u0000\u0000PR\b\u0002\u0000\u0000QP\u0001"+
		"\u0000\u0000\u0000RS\u0001\u0000\u0000\u0000SQ\u0001\u0000\u0000\u0000"+
		"ST\u0001\u0000\u0000\u0000T\u001d\u0001\u0000\u0000\u0000UV\u0003\u0004"+
		"\u0000\u0000VW\u0001\u0000\u0000\u0000WX\u0006\r\u0004\u0000X\u001f\u0001"+
		"\u0000\u0000\u0000Y[\b\u0003\u0000\u0000ZY\u0001\u0000\u0000\u0000[\\"+
		"\u0001\u0000\u0000\u0000\\Z\u0001\u0000\u0000\u0000\\]\u0001\u0000\u0000"+
		"\u0000]!\u0001\u0000\u0000\u0000^_\u0003\b\u0002\u0000_`\u0001\u0000\u0000"+
		"\u0000`a\u0006\u000f\u0003\u0000a#\u0001\u0000\u0000\u0000bc\u0003\u0006"+
		"\u0001\u0000cd\u0001\u0000\u0000\u0000de\u0006\u0010\u0004\u0000e%\u0001"+
		"\u0000\u0000\u0000fh\b\u0004\u0000\u0000gf\u0001\u0000\u0000\u0000hi\u0001"+
		"\u0000\u0000\u0000ig\u0001\u0000\u0000\u0000ij\u0001\u0000\u0000\u0000"+
		"j\'\u0001\u0000\u0000\u0000kl\u0003\b\u0002\u0000lm\u0001\u0000\u0000"+
		"\u0000mn\u0006\u0012\u0004\u0000n)\u0001\u0000\u0000\u0000\t\u0000\u0001"+
		"\u0002\u00033BS\\i\u0005\u0006\u0000\u0000\u0005\u0001\u0000\u0005\u0002"+
		"\u0000\u0005\u0003\u0000\u0004\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}