// Generated from /Users/jakubwadrzyk/Documents/Programing/Python/Kompilatory/DepotGrammar/grammar/DepotLexer.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class DepotLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		COMMA=1, COLON=2, LCURLY=3, RCURLY=4, DEPOT=5, SECTION=6, SECTIONS=7, 
		PRODUCT=8, CATEGORY=9, UNIT=10, UNIT_NAME=11, EMPLOYEES=12, EMPLOYEE=13, 
		DATE_SEP=14, ID=15, DATE=16, INT=17, WS=18;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"COMMA", "COLON", "LCURLY", "RCURLY", "DEPOT", "SECTION", "SECTIONS", 
			"PRODUCT", "CATEGORY", "UNIT", "UNIT_NAME", "EMPLOYEES", "EMPLOYEE", 
			"DATE_SEP", "ID", "DATE", "INT", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "','", "':'", "'{'", "'}'", "'DEPOT'", "'SECTION'", "'SECTIONS'", 
			"'PRODUCT'", "'CATEGORY'", "'UNIT'", null, "'EMPLOYEES'", "'EMPLOYEE'", 
			"'/'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "COMMA", "COLON", "LCURLY", "RCURLY", "DEPOT", "SECTION", "SECTIONS", 
			"PRODUCT", "CATEGORY", "UNIT", "UNIT_NAME", "EMPLOYEES", "EMPLOYEE", 
			"DATE_SEP", "ID", "DATE", "INT", "WS"
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


	public DepotLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "DepotLexer.g4"; }

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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\24\u0095\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3"+
		"\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b"+
		"\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3"+
		"\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\ff\n\f\3"+
		"\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3"+
		"\16\3\16\3\16\3\17\3\17\3\20\3\20\7\20\177\n\20\f\20\16\20\u0082\13\20"+
		"\3\21\3\21\3\21\3\21\3\21\3\21\3\22\6\22\u008b\n\22\r\22\16\22\u008c\3"+
		"\23\6\23\u0090\n\23\r\23\16\23\u0091\3\23\3\23\2\2\24\3\3\5\4\7\5\t\6"+
		"\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24"+
		"\3\2\6\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\5\2\13\f\16\17\"\"\2\u009b\2"+
		"\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2"+
		"\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2"+
		"\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2"+
		"\2\2%\3\2\2\2\3\'\3\2\2\2\5)\3\2\2\2\7+\3\2\2\2\t-\3\2\2\2\13/\3\2\2\2"+
		"\r\65\3\2\2\2\17=\3\2\2\2\21F\3\2\2\2\23N\3\2\2\2\25W\3\2\2\2\27e\3\2"+
		"\2\2\31g\3\2\2\2\33q\3\2\2\2\35z\3\2\2\2\37|\3\2\2\2!\u0083\3\2\2\2#\u008a"+
		"\3\2\2\2%\u008f\3\2\2\2\'(\7.\2\2(\4\3\2\2\2)*\7<\2\2*\6\3\2\2\2+,\7}"+
		"\2\2,\b\3\2\2\2-.\7\177\2\2.\n\3\2\2\2/\60\7F\2\2\60\61\7G\2\2\61\62\7"+
		"R\2\2\62\63\7Q\2\2\63\64\7V\2\2\64\f\3\2\2\2\65\66\7U\2\2\66\67\7G\2\2"+
		"\678\7E\2\289\7V\2\29:\7K\2\2:;\7Q\2\2;<\7P\2\2<\16\3\2\2\2=>\7U\2\2>"+
		"?\7G\2\2?@\7E\2\2@A\7V\2\2AB\7K\2\2BC\7Q\2\2CD\7P\2\2DE\7U\2\2E\20\3\2"+
		"\2\2FG\7R\2\2GH\7T\2\2HI\7Q\2\2IJ\7F\2\2JK\7W\2\2KL\7E\2\2LM\7V\2\2M\22"+
		"\3\2\2\2NO\7E\2\2OP\7C\2\2PQ\7V\2\2QR\7G\2\2RS\7I\2\2ST\7Q\2\2TU\7T\2"+
		"\2UV\7[\2\2V\24\3\2\2\2WX\7W\2\2XY\7P\2\2YZ\7K\2\2Z[\7V\2\2[\26\3\2\2"+
		"\2\\]\7r\2\2]f\7e\2\2^_\7m\2\2_f\7i\2\2`f\4no\2ab\7o\2\2bf\7\64\2\2cd"+
		"\7o\2\2df\7\65\2\2e\\\3\2\2\2e^\3\2\2\2e`\3\2\2\2ea\3\2\2\2ec\3\2\2\2"+
		"f\30\3\2\2\2gh\7G\2\2hi\7O\2\2ij\7R\2\2jk\7N\2\2kl\7Q\2\2lm\7[\2\2mn\7"+
		"G\2\2no\7G\2\2op\7U\2\2p\32\3\2\2\2qr\7G\2\2rs\7O\2\2st\7R\2\2tu\7N\2"+
		"\2uv\7Q\2\2vw\7[\2\2wx\7G\2\2xy\7G\2\2y\34\3\2\2\2z{\7\61\2\2{\36\3\2"+
		"\2\2|\u0080\t\2\2\2}\177\t\3\2\2~}\3\2\2\2\177\u0082\3\2\2\2\u0080~\3"+
		"\2\2\2\u0080\u0081\3\2\2\2\u0081 \3\2\2\2\u0082\u0080\3\2\2\2\u0083\u0084"+
		"\5#\22\2\u0084\u0085\5\35\17\2\u0085\u0086\5#\22\2\u0086\u0087\5\35\17"+
		"\2\u0087\u0088\5#\22\2\u0088\"\3\2\2\2\u0089\u008b\t\4\2\2\u008a\u0089"+
		"\3\2\2\2\u008b\u008c\3\2\2\2\u008c\u008a\3\2\2\2\u008c\u008d\3\2\2\2\u008d"+
		"$\3\2\2\2\u008e\u0090\t\5\2\2\u008f\u008e\3\2\2\2\u0090\u0091\3\2\2\2"+
		"\u0091\u008f\3\2\2\2\u0091\u0092\3\2\2\2\u0092\u0093\3\2\2\2\u0093\u0094"+
		"\b\23\2\2\u0094&\3\2\2\2\7\2e\u0080\u008c\u0091\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}