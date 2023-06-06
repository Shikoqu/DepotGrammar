// Generated from /Users/jakubwadrzyk/Documents/Programing/Python/Kompilatory/DepotGrammar/grammar/DepotParser.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class DepotParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		COMMA=1, COLON=2, LCURLY=3, RCURLY=4, DEPOT=5, SECTION=6, SECTIONS=7, 
		PRODUCT=8, CATEGORY=9, UNIT=10, UNIT_NAME=11, EMPLOYEES=12, EMPLOYEE=13, 
		DATE_SEP=14, ID=15, DATE=16, INT=17, WS=18;
	public static final int
		RULE_program = 0, RULE_depot = 1, RULE_depot_name = 2, RULE_depot_body = 3, 
		RULE_section_list = 4, RULE_section = 5, RULE_section_name = 6, RULE_section_body = 7, 
		RULE_product = 8, RULE_product_name = 9, RULE_product_body = 10, RULE_category = 11, 
		RULE_category_name = 12, RULE_quantity = 13, RULE_unit = 14, RULE_unit_name = 15, 
		RULE_employee_list = 16, RULE_employees_body = 17, RULE_employee = 18, 
		RULE_employee_body = 19, RULE_employee_sections = 20, RULE_name = 21, 
		RULE_surname = 22, RULE_office = 23, RULE_employment_date = 24;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "depot", "depot_name", "depot_body", "section_list", "section", 
			"section_name", "section_body", "product", "product_name", "product_body", 
			"category", "category_name", "quantity", "unit", "unit_name", "employee_list", 
			"employees_body", "employee", "employee_body", "employee_sections", "name", 
			"surname", "office", "employment_date"
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

	@Override
	public String getGrammarFileName() { return "DepotParser.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public DepotParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public DepotContext depot() {
			return getRuleContext(DepotContext.class,0);
		}
		public TerminalNode EOF() { return getToken(DepotParser.EOF, 0); }
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(50);
			depot();
			setState(51);
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

	public static class DepotContext extends ParserRuleContext {
		public TerminalNode DEPOT() { return getToken(DepotParser.DEPOT, 0); }
		public Depot_nameContext depot_name() {
			return getRuleContext(Depot_nameContext.class,0);
		}
		public Depot_bodyContext depot_body() {
			return getRuleContext(Depot_bodyContext.class,0);
		}
		public DepotContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_depot; }
	}

	public final DepotContext depot() throws RecognitionException {
		DepotContext _localctx = new DepotContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_depot);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(53);
			match(DEPOT);
			setState(54);
			depot_name();
			setState(55);
			depot_body();
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

	public static class Depot_nameContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(DepotParser.ID, 0); }
		public Depot_nameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_depot_name; }
	}

	public final Depot_nameContext depot_name() throws RecognitionException {
		Depot_nameContext _localctx = new Depot_nameContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_depot_name);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(57);
			match(ID);
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

	public static class Depot_bodyContext extends ParserRuleContext {
		public TerminalNode LCURLY() { return getToken(DepotParser.LCURLY, 0); }
		public Section_listContext section_list() {
			return getRuleContext(Section_listContext.class,0);
		}
		public Employee_listContext employee_list() {
			return getRuleContext(Employee_listContext.class,0);
		}
		public TerminalNode RCURLY() { return getToken(DepotParser.RCURLY, 0); }
		public Depot_bodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_depot_body; }
	}

	public final Depot_bodyContext depot_body() throws RecognitionException {
		Depot_bodyContext _localctx = new Depot_bodyContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_depot_body);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(59);
			match(LCURLY);
			setState(60);
			section_list();
			setState(61);
			employee_list();
			setState(62);
			match(RCURLY);
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

	public static class Section_listContext extends ParserRuleContext {
		public List<SectionContext> section() {
			return getRuleContexts(SectionContext.class);
		}
		public SectionContext section(int i) {
			return getRuleContext(SectionContext.class,i);
		}
		public Section_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_section_list; }
	}

	public final Section_listContext section_list() throws RecognitionException {
		Section_listContext _localctx = new Section_listContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_section_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(67);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==SECTION) {
				{
				{
				setState(64);
				section();
				}
				}
				setState(69);
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

	public static class SectionContext extends ParserRuleContext {
		public TerminalNode SECTION() { return getToken(DepotParser.SECTION, 0); }
		public Section_nameContext section_name() {
			return getRuleContext(Section_nameContext.class,0);
		}
		public Section_bodyContext section_body() {
			return getRuleContext(Section_bodyContext.class,0);
		}
		public SectionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_section; }
	}

	public final SectionContext section() throws RecognitionException {
		SectionContext _localctx = new SectionContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_section);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(70);
			match(SECTION);
			setState(71);
			section_name();
			setState(72);
			section_body();
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

	public static class Section_nameContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(DepotParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(DepotParser.ID, i);
		}
		public Section_nameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_section_name; }
	}

	public final Section_nameContext section_name() throws RecognitionException {
		Section_nameContext _localctx = new Section_nameContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_section_name);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(75); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(74);
				match(ID);
				}
				}
				setState(77); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==ID );
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

	public static class Section_bodyContext extends ParserRuleContext {
		public TerminalNode LCURLY() { return getToken(DepotParser.LCURLY, 0); }
		public TerminalNode RCURLY() { return getToken(DepotParser.RCURLY, 0); }
		public List<ProductContext> product() {
			return getRuleContexts(ProductContext.class);
		}
		public ProductContext product(int i) {
			return getRuleContext(ProductContext.class,i);
		}
		public Section_bodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_section_body; }
	}

	public final Section_bodyContext section_body() throws RecognitionException {
		Section_bodyContext _localctx = new Section_bodyContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_section_body);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(79);
			match(LCURLY);
			setState(83);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==PRODUCT) {
				{
				{
				setState(80);
				product();
				}
				}
				setState(85);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(86);
			match(RCURLY);
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

	public static class ProductContext extends ParserRuleContext {
		public TerminalNode PRODUCT() { return getToken(DepotParser.PRODUCT, 0); }
		public Product_nameContext product_name() {
			return getRuleContext(Product_nameContext.class,0);
		}
		public Product_bodyContext product_body() {
			return getRuleContext(Product_bodyContext.class,0);
		}
		public ProductContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_product; }
	}

	public final ProductContext product() throws RecognitionException {
		ProductContext _localctx = new ProductContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_product);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(88);
			match(PRODUCT);
			setState(89);
			product_name();
			setState(90);
			product_body();
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

	public static class Product_nameContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(DepotParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(DepotParser.ID, i);
		}
		public Product_nameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_product_name; }
	}

	public final Product_nameContext product_name() throws RecognitionException {
		Product_nameContext _localctx = new Product_nameContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_product_name);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(93); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(92);
				match(ID);
				}
				}
				setState(95); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==ID );
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

	public static class Product_bodyContext extends ParserRuleContext {
		public TerminalNode LCURLY() { return getToken(DepotParser.LCURLY, 0); }
		public CategoryContext category() {
			return getRuleContext(CategoryContext.class,0);
		}
		public List<TerminalNode> COMMA() { return getTokens(DepotParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(DepotParser.COMMA, i);
		}
		public QuantityContext quantity() {
			return getRuleContext(QuantityContext.class,0);
		}
		public UnitContext unit() {
			return getRuleContext(UnitContext.class,0);
		}
		public TerminalNode RCURLY() { return getToken(DepotParser.RCURLY, 0); }
		public Product_bodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_product_body; }
	}

	public final Product_bodyContext product_body() throws RecognitionException {
		Product_bodyContext _localctx = new Product_bodyContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_product_body);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(97);
			match(LCURLY);
			setState(98);
			category();
			setState(99);
			match(COMMA);
			setState(100);
			quantity();
			setState(101);
			match(COMMA);
			setState(102);
			unit();
			setState(103);
			match(RCURLY);
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

	public static class CategoryContext extends ParserRuleContext {
		public TerminalNode CATEGORY() { return getToken(DepotParser.CATEGORY, 0); }
		public Category_nameContext category_name() {
			return getRuleContext(Category_nameContext.class,0);
		}
		public CategoryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_category; }
	}

	public final CategoryContext category() throws RecognitionException {
		CategoryContext _localctx = new CategoryContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_category);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(105);
			match(CATEGORY);
			setState(106);
			category_name();
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

	public static class Category_nameContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(DepotParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(DepotParser.ID, i);
		}
		public Category_nameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_category_name; }
	}

	public final Category_nameContext category_name() throws RecognitionException {
		Category_nameContext _localctx = new Category_nameContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_category_name);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(109); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(108);
				match(ID);
				}
				}
				setState(111); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==ID );
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

	public static class QuantityContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(DepotParser.INT, 0); }
		public QuantityContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_quantity; }
	}

	public final QuantityContext quantity() throws RecognitionException {
		QuantityContext _localctx = new QuantityContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_quantity);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(113);
			match(INT);
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

	public static class UnitContext extends ParserRuleContext {
		public TerminalNode UNIT() { return getToken(DepotParser.UNIT, 0); }
		public Unit_nameContext unit_name() {
			return getRuleContext(Unit_nameContext.class,0);
		}
		public UnitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unit; }
	}

	public final UnitContext unit() throws RecognitionException {
		UnitContext _localctx = new UnitContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_unit);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(115);
			match(UNIT);
			setState(116);
			unit_name();
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

	public static class Unit_nameContext extends ParserRuleContext {
		public TerminalNode UNIT_NAME() { return getToken(DepotParser.UNIT_NAME, 0); }
		public Unit_nameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unit_name; }
	}

	public final Unit_nameContext unit_name() throws RecognitionException {
		Unit_nameContext _localctx = new Unit_nameContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_unit_name);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(118);
			match(UNIT_NAME);
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

	public static class Employee_listContext extends ParserRuleContext {
		public TerminalNode EMPLOYEES() { return getToken(DepotParser.EMPLOYEES, 0); }
		public Employees_bodyContext employees_body() {
			return getRuleContext(Employees_bodyContext.class,0);
		}
		public Employee_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_employee_list; }
	}

	public final Employee_listContext employee_list() throws RecognitionException {
		Employee_listContext _localctx = new Employee_listContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_employee_list);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(120);
			match(EMPLOYEES);
			setState(121);
			employees_body();
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

	public static class Employees_bodyContext extends ParserRuleContext {
		public TerminalNode LCURLY() { return getToken(DepotParser.LCURLY, 0); }
		public TerminalNode RCURLY() { return getToken(DepotParser.RCURLY, 0); }
		public List<EmployeeContext> employee() {
			return getRuleContexts(EmployeeContext.class);
		}
		public EmployeeContext employee(int i) {
			return getRuleContext(EmployeeContext.class,i);
		}
		public Employees_bodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_employees_body; }
	}

	public final Employees_bodyContext employees_body() throws RecognitionException {
		Employees_bodyContext _localctx = new Employees_bodyContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_employees_body);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(123);
			match(LCURLY);
			setState(127);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==EMPLOYEE) {
				{
				{
				setState(124);
				employee();
				}
				}
				setState(129);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(130);
			match(RCURLY);
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

	public static class EmployeeContext extends ParserRuleContext {
		public TerminalNode EMPLOYEE() { return getToken(DepotParser.EMPLOYEE, 0); }
		public NameContext name() {
			return getRuleContext(NameContext.class,0);
		}
		public SurnameContext surname() {
			return getRuleContext(SurnameContext.class,0);
		}
		public Employee_bodyContext employee_body() {
			return getRuleContext(Employee_bodyContext.class,0);
		}
		public EmployeeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_employee; }
	}

	public final EmployeeContext employee() throws RecognitionException {
		EmployeeContext _localctx = new EmployeeContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_employee);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(132);
			match(EMPLOYEE);
			setState(133);
			name();
			setState(134);
			surname();
			setState(135);
			employee_body();
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

	public static class Employee_bodyContext extends ParserRuleContext {
		public TerminalNode LCURLY() { return getToken(DepotParser.LCURLY, 0); }
		public OfficeContext office() {
			return getRuleContext(OfficeContext.class,0);
		}
		public List<TerminalNode> COMMA() { return getTokens(DepotParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(DepotParser.COMMA, i);
		}
		public Employment_dateContext employment_date() {
			return getRuleContext(Employment_dateContext.class,0);
		}
		public Employee_sectionsContext employee_sections() {
			return getRuleContext(Employee_sectionsContext.class,0);
		}
		public TerminalNode RCURLY() { return getToken(DepotParser.RCURLY, 0); }
		public Employee_bodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_employee_body; }
	}

	public final Employee_bodyContext employee_body() throws RecognitionException {
		Employee_bodyContext _localctx = new Employee_bodyContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_employee_body);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(137);
			match(LCURLY);
			setState(138);
			office();
			setState(139);
			match(COMMA);
			setState(140);
			employment_date();
			setState(141);
			match(COMMA);
			setState(142);
			employee_sections();
			setState(143);
			match(RCURLY);
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

	public static class Employee_sectionsContext extends ParserRuleContext {
		public TerminalNode SECTION() { return getToken(DepotParser.SECTION, 0); }
		public List<Section_nameContext> section_name() {
			return getRuleContexts(Section_nameContext.class);
		}
		public Section_nameContext section_name(int i) {
			return getRuleContext(Section_nameContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(DepotParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(DepotParser.COMMA, i);
		}
		public Employee_sectionsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_employee_sections; }
	}

	public final Employee_sectionsContext employee_sections() throws RecognitionException {
		Employee_sectionsContext _localctx = new Employee_sectionsContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_employee_sections);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(145);
			match(SECTION);
			setState(146);
			section_name();
			setState(151);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(147);
				match(COMMA);
				setState(148);
				section_name();
				}
				}
				setState(153);
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

	public static class NameContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(DepotParser.ID, 0); }
		public NameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_name; }
	}

	public final NameContext name() throws RecognitionException {
		NameContext _localctx = new NameContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_name);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(154);
			match(ID);
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

	public static class SurnameContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(DepotParser.ID, 0); }
		public SurnameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_surname; }
	}

	public final SurnameContext surname() throws RecognitionException {
		SurnameContext _localctx = new SurnameContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_surname);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(156);
			match(ID);
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

	public static class OfficeContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(DepotParser.ID, 0); }
		public OfficeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_office; }
	}

	public final OfficeContext office() throws RecognitionException {
		OfficeContext _localctx = new OfficeContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_office);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(158);
			match(ID);
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

	public static class Employment_dateContext extends ParserRuleContext {
		public TerminalNode DATE() { return getToken(DepotParser.DATE, 0); }
		public Employment_dateContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_employment_date; }
	}

	public final Employment_dateContext employment_date() throws RecognitionException {
		Employment_dateContext _localctx = new Employment_dateContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_employment_date);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(160);
			match(DATE);
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\24\u00a5\4\2\t\2"+
		"\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6"+
		"\7\6D\n\6\f\6\16\6G\13\6\3\7\3\7\3\7\3\7\3\b\6\bN\n\b\r\b\16\bO\3\t\3"+
		"\t\7\tT\n\t\f\t\16\tW\13\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13\6\13`\n\13\r\13"+
		"\16\13a\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\16\6\16p\n\16\r"+
		"\16\16\16q\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\22\3\22\3\22\3\23\3\23"+
		"\7\23\u0080\n\23\f\23\16\23\u0083\13\23\3\23\3\23\3\24\3\24\3\24\3\24"+
		"\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\7\26"+
		"\u0098\n\26\f\26\16\26\u009b\13\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32"+
		"\3\32\3\32\2\2\33\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62"+
		"\2\2\2\u0092\2\64\3\2\2\2\4\67\3\2\2\2\6;\3\2\2\2\b=\3\2\2\2\nE\3\2\2"+
		"\2\fH\3\2\2\2\16M\3\2\2\2\20Q\3\2\2\2\22Z\3\2\2\2\24_\3\2\2\2\26c\3\2"+
		"\2\2\30k\3\2\2\2\32o\3\2\2\2\34s\3\2\2\2\36u\3\2\2\2 x\3\2\2\2\"z\3\2"+
		"\2\2$}\3\2\2\2&\u0086\3\2\2\2(\u008b\3\2\2\2*\u0093\3\2\2\2,\u009c\3\2"+
		"\2\2.\u009e\3\2\2\2\60\u00a0\3\2\2\2\62\u00a2\3\2\2\2\64\65\5\4\3\2\65"+
		"\66\7\2\2\3\66\3\3\2\2\2\678\7\7\2\289\5\6\4\29:\5\b\5\2:\5\3\2\2\2;<"+
		"\7\21\2\2<\7\3\2\2\2=>\7\5\2\2>?\5\n\6\2?@\5\"\22\2@A\7\6\2\2A\t\3\2\2"+
		"\2BD\5\f\7\2CB\3\2\2\2DG\3\2\2\2EC\3\2\2\2EF\3\2\2\2F\13\3\2\2\2GE\3\2"+
		"\2\2HI\7\b\2\2IJ\5\16\b\2JK\5\20\t\2K\r\3\2\2\2LN\7\21\2\2ML\3\2\2\2N"+
		"O\3\2\2\2OM\3\2\2\2OP\3\2\2\2P\17\3\2\2\2QU\7\5\2\2RT\5\22\n\2SR\3\2\2"+
		"\2TW\3\2\2\2US\3\2\2\2UV\3\2\2\2VX\3\2\2\2WU\3\2\2\2XY\7\6\2\2Y\21\3\2"+
		"\2\2Z[\7\n\2\2[\\\5\24\13\2\\]\5\26\f\2]\23\3\2\2\2^`\7\21\2\2_^\3\2\2"+
		"\2`a\3\2\2\2a_\3\2\2\2ab\3\2\2\2b\25\3\2\2\2cd\7\5\2\2de\5\30\r\2ef\7"+
		"\3\2\2fg\5\34\17\2gh\7\3\2\2hi\5\36\20\2ij\7\6\2\2j\27\3\2\2\2kl\7\13"+
		"\2\2lm\5\32\16\2m\31\3\2\2\2np\7\21\2\2on\3\2\2\2pq\3\2\2\2qo\3\2\2\2"+
		"qr\3\2\2\2r\33\3\2\2\2st\7\23\2\2t\35\3\2\2\2uv\7\f\2\2vw\5 \21\2w\37"+
		"\3\2\2\2xy\7\r\2\2y!\3\2\2\2z{\7\16\2\2{|\5$\23\2|#\3\2\2\2}\u0081\7\5"+
		"\2\2~\u0080\5&\24\2\177~\3\2\2\2\u0080\u0083\3\2\2\2\u0081\177\3\2\2\2"+
		"\u0081\u0082\3\2\2\2\u0082\u0084\3\2\2\2\u0083\u0081\3\2\2\2\u0084\u0085"+
		"\7\6\2\2\u0085%\3\2\2\2\u0086\u0087\7\17\2\2\u0087\u0088\5,\27\2\u0088"+
		"\u0089\5.\30\2\u0089\u008a\5(\25\2\u008a\'\3\2\2\2\u008b\u008c\7\5\2\2"+
		"\u008c\u008d\5\60\31\2\u008d\u008e\7\3\2\2\u008e\u008f\5\62\32\2\u008f"+
		"\u0090\7\3\2\2\u0090\u0091\5*\26\2\u0091\u0092\7\6\2\2\u0092)\3\2\2\2"+
		"\u0093\u0094\7\b\2\2\u0094\u0099\5\16\b\2\u0095\u0096\7\3\2\2\u0096\u0098"+
		"\5\16\b\2\u0097\u0095\3\2\2\2\u0098\u009b\3\2\2\2\u0099\u0097\3\2\2\2"+
		"\u0099\u009a\3\2\2\2\u009a+\3\2\2\2\u009b\u0099\3\2\2\2\u009c\u009d\7"+
		"\21\2\2\u009d-\3\2\2\2\u009e\u009f\7\21\2\2\u009f/\3\2\2\2\u00a0\u00a1"+
		"\7\21\2\2\u00a1\61\3\2\2\2\u00a2\u00a3\7\22\2\2\u00a3\63\3\2\2\2\tEOU"+
		"aq\u0081\u0099";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}