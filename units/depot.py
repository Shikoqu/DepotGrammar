from typing import List, Optional

from .employee import Employee
from .section import Section


class Depot:
    def __init__(self,
                 name: str = None,
                 sections: Optional[List[Section]] = None,
                 employees: Optional[List[Employee]] = None):
        self.name: str = name
        self.sections: List[Section] = sections or []
        self.employees: List[Employee] = employees or []
        
    def normalize(self):            
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
        
    
    def add_section(self, section):
        self.sections.append(section)
        
    def add_employee(self, employee):
        self.employees.append(employee)
        
    
    def contains_product(self, product_name):
        for section in self.sections:
            if section.contains_product(product_name):
                return True
        return False
    
    def find_product(self, product_name):
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
    
    def save(self, indent='') -> str:
        str_builder = indent + f'DEPOT {self.name}' + ' {\n'
        
        for section in self.sections:
            str_builder += section.save(indent + '\t') + '\n'
        
        if len(self.employees) > 0:
            str_builder += indent + '\t' + 'EMPLOYEES {\n'
            for employee in self.employees:
                str_builder += employee.save(indent + '\t\t') + '\n'
            str_builder += indent + '\t' +'}\n'
        
        str_builder += indent + '}'
        return str_builder
    
