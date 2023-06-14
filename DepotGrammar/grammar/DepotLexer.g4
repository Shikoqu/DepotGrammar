lexer grammar DepotLexer;

COMMA: ',';
COLON: ':';
LCURLY: '{';
RCURLY: '}';

DEPOT: 'DEPOT';
SECTION: 'SECTION';
SECTIONS: 'SECTIONS';
PRODUCT: 'PRODUCT';
CATEGORY: 'CATEGORY';
UNIT: 'UNIT';
UNIT_NAME: 'pc' | 'kg' | 'l' | 'm' | 'm2' | 'm3';
EMPLOYEES: 'EMPLOYEES';
EMPLOYEE: 'EMPLOYEE';

DATE_SEP: '/';

ID: [a-zA-Z_][a-zA-Z0-9_]*;

DATE: INT DATE_SEP INT DATE_SEP INT;

INT: [0-9]+;
WS: [ \t\n\r\f]+ -> skip;

