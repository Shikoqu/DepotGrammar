from datetime import date
from antlr4 import *

from DepotListener import DepotListener
from grammar import DepotLexer, DepotParser

from units.employee import Employee
from units.product import Product

def parse(code: str) -> DepotParser:
    # Utwórz strumień wejściowy dla analizy składniowej
    input_stream = InputStream(code)

    # Utwórz lekser
    lexer = DepotLexer(input_stream)
    token_stream = CommonTokenStream(lexer)

    # Utwórz parser
    parser = DepotParser(token_stream)
    
    return parser


def main():
    code = open('example.txt').read()

    parser = parse(code)
    tree = parser.program()

    # Utwórz instancję listenera
    listener = DepotListener()

    # Przechodź przez drzewo rozbioru i wywołuj metody listenera
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    my_depot = listener.depot

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
    
    
    


if __name__ == '__main__':
    main()