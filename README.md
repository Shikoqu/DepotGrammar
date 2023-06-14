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
  Inicjalizacją magazynu zajmuje się biblioteczna funkcja ```DepotGrammar.read()```, zwraza ona obiekt klasy *Depot*.
  Przykład użycia:
  ```python
  my_depot = DepotGrammar.read('example.txt')
  ```

  Klasa *Depot* jest główną klasą biblioteki, zawiera ona wszystkie informacje o magazynie, posiada ona następujące atrybuty:
  * ```name: str``` - nazwa magazynu
  * ```sections: SectionList``` - lista sekcji magazynu
  * ```employees: EmployeeList``` - lista pracowników magazynu

  Dzięki temu że klasy *SectionList*, *ProductList* i *EmployeeList* dziedziczą po klasie *UnitList* można na nich wykonywać podobne operacje takie jak:
  * ```find(unit)``` - zwraca obiekt klasy *Unit* o podanym kluczu
  * ```filter(filter=None)``` - zwraca listę obiektów klasy *Unit* spełniających podany filtr
  * ```sort(key=None)``` - sortuje listę po kluczu
  * ```sort_inplace(key=None)``` - sortuje listę po kluczu w miejscu
  * ```add(unit)``` - dodaje obiekt klasy *Unit* do listy
  * ```add_all(unit_list: UnitList | List[Unit])``` - dodaje wszystkie obiekty klasy *Unit* z listy do listy
  * ```normalize()``` - łączy obiekty o takim samym kluczu i normalizuje wszystkie obiekty w liście
  Klasa *SectionList* zawiera dodatkowo następujące metody:
  * ```contains(section)``` - sprawdza czy lista zawiera podany obiekt klasy *Section*
  * ```contains_all(section_list: SectionList | List[Section])``` - sprawdza czy lista zawiera wszystkie obiekty klasy *Section* z listy
  * ```contains_any(section_list: SectionList | List[Section])``` - sprawdza czy lista zawiera jakikolwiek obiekt klasy *Section* z listy

  Klasa *Unit* jest abstrakcyjną klasą bazową dla klas *Section*, *Product* i *Employee*, zawiera ona następujące metody:
  * ```key``` - zwraca klucz obiektu
  * ```normalize()``` - normalizuje obiekt
  * ```merge(unit)``` - łączy obiekt z podanym obiektem
  * ```__str__()``` - zwraca reprezentację obiektu w postaci stringa zgodnego z gramatyką

  Klasa *Section* dziedziczy po klasie *Unit*, zawiera ona następujące atrybuty:
  * ```name: str``` - nazwa sekcji
  * ```products: ProductList``` - lista produktów w sekcji
  Klasa *Section* zawiera dodatkowo następujące metody:
  * ```contains(product)``` - sprawdza czy sekcja zawiera podany obiekt klasy *Product*
  * ```contains_all(product_list: ProductList | List[Product])``` - sprawdza czy sekcja zawiera wszystkie obiekty klasy *Product* z listy
  * ```contains_any(product_list: ProductList | List[Product])``` - sprawdza czy sekcja zawiera jakikolwiek obiekt klasy *Product* z listy

  Klasa *Product* dziedziczy po klasie *Unit*, zawiera ona następujące atrybuty:
  * ```name: str``` - nazwa produktu
  * ```category: str``` - kategoria produktu
  * ```quantity: int``` - ilość produktu
  * ```unit: str``` - jednostka liczności produktu sztuki, kilogramy, litry, metry, metry kwadratowe, metry sześcienne

  Klasa *Employee* dziedziczy po klasie *Unit*, zawiera ona następujące atrybuty:
  * ```depot: Depot``` - magazyn w którym pracuje pracownik - pomocniczy atrybut służący do wygodnego normalizacji pracownika
  * ```name: str``` - imię pracownika
  * ```surname: str``` - nazwisko pracownika
  * ```office: str``` - stanowisko pracownika
  * ```employment_date: datetime.date``` - data zatrudnienia pracownika
  * ```sections: SectionList``` - lista sekcji w których pracuje pracownik

  Te wszystkie metody i atrybuty są wygodnym sposobem na zarządzanie, edytowanie i przeszukiwanie magazynu:
  ```python
    my_depot = DepotGrammar.read('example.txt')

    print(my_depot)
    my_depot.employees.add(Employee(my_depot, 'Krystian', 'Sitarz', 'Kierownik', date(2020, 1, 1)))
    print(my_depot)
    
    
    print('\nPracownicy:')
    e0 = my_depot.employees.data[0]
    e1 = my_depot.employees.find(key=('Anna', 'Nowak'))
    print(e0, '\n', e1)
    
    print('\nKierownicy:')
    ks = my_depot.employees.filter(lambda e: e.office == 'Kierownik')
    for k in ks:
        print(k.name, k.surname, k.office)
    
    print('\nSekcje z koszulkami lub Laptopami:')
    es = my_depot.sections.filter(lambda s: s.contains_any([Product('Koszulka'), Product('Laptop')], product_filter=lambda p: p.name)) or []
    for e in es:
        print(e)
  ```

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
