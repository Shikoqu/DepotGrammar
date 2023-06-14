# DepotGrammar

### Członkowie zespołu:

Imię i nazwisko | e-mail
:---- | :---:
Mateusz Mirecki | [📧](mmirecki@student.agh.edu.pl)
Krystian Sitarz | [📧](ksitarz@student.agh.edu.pl)
Jakub Wądrzyk | [📧](jwadrzyk@student.agh.edu.pl)

---

### Do projektu wykorzystano:
  * [**Python 3.11.3**](https://www.python.org/)
    * język programowania w którym został napisany program
  * [**ANTLR4**](https://www.antlr.org/)
    * narzędzie pozwoliło na wygenerowanie parsera i lexera do gramatyki depot
  * [**ANTLR4-Python3-Runtime**](https://pypi.org/project/antlr4-python3-runtime/)
    * biblioteka do wygodnego korzystania z wygenerowanego parsera i lexera

---

## 1. Założenia programu
  * Stworzenie ogólnego języka opisu magazynu
  * Wraz z biblioteką do wygodnej obsługi w pythonie

---

## 2. Krótka instrukcja obsługi
  Klasa ```Depot``` jest główną klasą biblioteki. Inicjalizacją magazynu zajmuje się statyczna metoda klasy - ```Depot.from_file()```.
  
  Przykładowe uycie:
  ```python
  my_depot = Depot.from_file('example.txt')
  ```

  Klasa *Depot* posiada następujące metody:
  * ```metoda(argumenty)``` - opis

---

## 3. [Spis tokenów](./grammar/DepotLexer.g4)
  ```g4
  DEPOT
  SECTION
  SECTIONS
  PRODUCT
  CATEGORY
  UNIT
  EMPLOYEES
  EMPLOYEE

  ID: [a-zA-Z_][a-zA-Z0-9_]*
  INT: [0-9]+
  UNIT_NAME: 'pc' | 'kg' | 'l' | 'm' | 'm2' | 'm3'
  DATE: INT DATE_SEP INT DATE_SEP INT
  DATE_SEP: '/'

  ,
  :
  {
  }
  ```

---

## 4. [Gramatyka przetwarzanego formatu](./grammar/DepotParser.g4)
  ```g4
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
  employee_sections: 'SECTION' employee_section_name (',' employee_section_name)*;

  name: ID;
  surname: ID;
  office: ID;
  employment_date: DATE;
  employee_section_name: ID+;
  ```

---

## 5. [Przykład](./example.txt)
  ```depot
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
      EMPLOYEE Anna Nowak { Kierownik, 15/03/2022, SECTION Odziez, Elektronika }
    }
  }
  ```
