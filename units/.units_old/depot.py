from typing import List, Optional

from employee_list import EmployeeList
from employee import Employee
from section_list import SectionList
from section import Section
from product_list import ProductList
from product import Product
from unit import Unit


class Depot(Unit):
    """Class representing a depot.
    """
    def __init__(self,
                 name: str = None,
                 sections: Optional[SectionList] = None,
                 employees: Optional[EmployeeList] = None):
        """Initializes the depot.
        
        Args:
            - name (str, optional): Defaults to None.
            - sections (Optional[List[Section]], optional): Defaults to None.
            - employees (Optional[List[Employee]], optional): Defaults to None.
        """
        super().__init__(name)
        self.sections: SectionList = sections or SectionList()
        self.employees: EmployeeList = employees or EmployeeList()
        
    @property
    def key(self):
        return self.name
        
    def normalize(self):
        """Normalizes the depot.
        Sections with the same name are merged.
        """
        sections_norm = {}
        for section in self.sections:
            if section.name in sections_norm:
                sections_norm[section.name].products += section.products
            else:
                sections_norm[section.name] = section
        self.products = list(sections_norm.values())
        
        for section in self.sections:
            section.normalize()
        for employee in self.employees:
            employee.normalize(self.sections)
    
    
    def __iadd__(self, unit):
        """Adds a unit to the depot regarding unit type.
        
        - If the unit is a Section or Employee, it is added to the depot.
        - If the unit is a Depot, its sections and employees are added to the depot.
        - If the unit is a list of units, each of them is added to the depot.

        Args:
            - unit (Section, Emlpoyee, Depot or list of units):  to be added. 

        Raises:
            - TypeError: if the unit is not a Section, Employee, Depot or list of units.
        """
        if isinstance(unit, Section):
            self.add_section(unit)
        elif isinstance(unit, Employee):
            self.add_employee(unit)
        elif isinstance(unit, Depot):
            self.sections.extend(unit.sections)
            self.employees.extend(unit.employees)
            self.normalize()
        elif isinstance(unit, List):
            for u in unit:
                self.__iadd__(u)
        else:
            raise TypeError(f'Cannot add {type(unit)} to Depot')
        return self
    
    def add_section(self, section: Section):
        """Adds a section to the depot.
        
        If section with the same name does already exist - merges them.
        """
        if self.contains_section(section.name):
            for s in self.sections:
                if s.name == section.name:
                    s += section
        self.sections.append(section)
    
    def add_employee(self, employee: Employee):
        """Adds an employee to the depot.
        """
        self.employees.append(employee)
    
    
    def contains_product(self, product_name: str) -> bool:
        """Checks if the depot contains a product with the given name.
        """
        for section in self.sections:
            if section.contains_product(product_name):
                return True
        return False
    
    def contains_section(self, section_name: str) -> bool:
        """Checks if the depot contains a section with the given name.
        """
        return section_name in [section.name for section in self.sections]
    
    def contains_employee(self, employee_name: str, employee_surname: str) -> bool:
        """Checks if the depot contains an employee with the given name and surname.
        """
        return (employee_name, employee_surname) in [(employee.name, employee.surname) for employee in self.employees]
    
    
    def select_section(self, section_name: str) -> Section:
        """Returns a section with the given name.
        
        Assumes that there is only one section with the given name.
        """
        for section in self.sections:
            if section.name == section_name:
                return section
        return None
    
    def select_employee(self, employee_name: str, employee_surname: str) -> Employee:
        """Returns an employee with the given name and surname.
        
        Assumes that there is only one employee with the given name and surname.
        """
        for employee in self.employees:
            if employee.name == employee_name and employee.surname == employee_surname:
                return employee
        return None

    def select_product(self, product_name: str, product_category: str) -> Product:
        """Returns a product with the given name and category.
        """
        for section in self.sections:
            for product in section.products:
                if product.name == product_name and product.category == product_category:
                    return product
    
    
    def find_product(self, product_name: str) -> List[Section]:
        """Returns sections containing a product with the given name and category.
        """
        sections = []
        product = None
        
        for section in self.sections:
            for product in section.products:
                if product.name == product_name:
                    sections.append(section)
        
    
    def __str__(self, indent='') -> str:
        str_builder = indent + f'DEPOT {self.name}' + ' {\n'
        
        for section in self.sections:
            str_builder += section.__str__(indent + '\t') + '\n'
        
        if len(self.employees) > 0:
            str_builder += indent + '\t' + 'EMPLOYEES {\n'
            for employee in self.employees:
                str_builder += employee.__str__(indent + '\t\t') + '\n'
            str_builder += indent + '\t' +'}\n'
        
        str_builder += indent + '}'
        return str_builder
    
    def save(self, filename: str):
        """Saves the depot to a file using depot grammar.
        
        Args:
            filename (str): Name of the file to be saved to.
        """
        with open(filename, 'w') as f:
            f.write(self.__str__())
    
