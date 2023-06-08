parser grammar DepotParser;
options {tokenVocab = DepotLexer;}

program: depot EOF;


depot: 'DEPOT' depot_name depot_body;
depot_name: ID;
depot_body: '{' section_list employee_list '}';


section_list: section*;
section: 'SECTION' section_name section_body;
section_name: ID+;
section_body: '{' product* '}';


product: 'PRODUCT' product_name product_body;
product_name: ID+;
product_body: '{' category ',' quantity ',' unit '}';

category: 'CATEGORY' category_name;
category_name: ID+;
quantity: INT;
unit: 'UNIT' unit_name;
unit_name: UNIT_NAME;


employee_list: 'EMPLOYEES' employees_body;
employees_body: '{' employee* '}';

employee: 'EMPLOYEE' name surname employee_body;
employee_body: '{' office ',' employment_date ',' employee_sections '}';
employee_sections:
	'SECTION' employee_section_name (',' employee_section_name)*;

name: ID;
surname: ID;
office: ID;
employment_date: DATE;
employee_section_name: ID+;

