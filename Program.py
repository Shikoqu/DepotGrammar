from datetime import date

import DepotGrammar
from DepotGrammar import Depot, Section, Product, Employee


def main():
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
    
    
    


if __name__ == '__main__':
    main()