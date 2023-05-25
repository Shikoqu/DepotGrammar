# Opis magazynu

### Członkowie zespołu:
  * Mateusz Mirecki: mmirecki@student.agh.edu.pl
  * Krystian Sitarz: ksitarz@student.agh.edu.pl
  * Jakub Wądrzyk: jwadrzyk@student.agh.edu.pl


## 1. Założenia programu
  * Stworzenie ogólnego języka opisu magazynu
  * Wraz z biblioteką do wygodnej obsługi w pythonie
        
## 2. Spis tokenów
```
  DEPOT
  SECTION
  PRODUCT
  CATEGORY
  UNIT
  EMPLOYEES
  EMPLOYEE
  {
  }
  ,
  ID: [a-zA-Z_][a-zA-Z0-9_]*
  INT: [0-9]+
  DATE: INT DATE_SEP INT DATE_SEP INT
  DATE_SEP: '/'
```

## 3. Gramatyka przetwarzanego formatu
```
  grammar ExprParser;

  program: depot EOF;
  |
  |
  depot: 'DEPOT' depot_name depot_body;
  depot_name: ID;
  depot_body: '{' section_list employee_list '}';
  |
  |
  section_list: section*;
  section: 'SECTION' section_name section_body;
  section_name: ID+;
  section_body: '{' product* '}';
  |
  |
  product: 'PRODUCT' product_name product_body;
  product_name: ID+;
  product_body: '{' category ',' quantity ',' unit '}';
  |
  category: 'CATEGORY' category_name;
  category_name: ID+;
  quantity: INT;
  unit: 'UNIT' ID;
  |
  |
  employee_list: 'EMPLOYEES' employees_body;
  employees_body: '{' employee* '}';
  |
  employee: 'EMPLOYEE' name surname employee_body;
  employee_body: '{' office ',' employment_date ',' employee_sections '}';
  employee_sections: 'SECTION' section_name (',' section_name)*;
  |
  name: ID;
  surname: ID;
  office: ID;
  employment_date: DATE;
  |
  |
  ID: [a|zA|Z_][a|zA|Z0|9_]*;
  INT: [0|9]+;
  DATE: INT DATE_SEP INT DATE_SEP INT;
  DATE_SEP: '/';
  |
  WS: [ \t\n\r\f]+ |> skip;
```

## 4. Informacja o stosowanych generatorach skanerów/parserów, pakietach zewnętrznych
Projekt jest tworzony w pythonie.
Do wygenerowania parseru oraz lexeru użyto narzędzia ANTLR4 dla pythona.

## 5. Krótka instrukcja obsługi

## 6. Przykład
```
  DEPOT Centralny {
    SECTION Elektronika {
      PRODUCT Laptop { CATEGORY Komputery, 10, UNIT pc }
      PRODUCT Smartfon { CATEGORY Telefony, 5, UNIT pc }
    }
    SECTION Odziez {
      PRODUCT Koszulka { CATEGORY Ubrania, 20, UNIT pc }
      PRODUCT Spodnie { CATEGORY Ubrania, 15, UNIT pc }
    }
    EMPLOYEES {
      EMPLOYEE Jan Kowalski { Magazynier, 01/01/2022, SECTION Elektronika }
      EMPLOYEE Anna Nowak { Kierownik, 15/03/2022, SECTION Odziez, Elektronika}
    }
  }
```
