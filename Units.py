from enum import Enum


class Depot:
    def __init__(self):
        self.name = None
        self.sections = []
        self.employees = []
    
    def __str__(self):
        str_builder = f'DEPOT {self.name}' + ' {\n'
        
        for section in self.sections:
            str_builder += str(section) + '\n'
        
        if len(self.employees) > 0:
            str_builder += '\t' + 'EMPLOYEES {\n'
            for employee in self.employees:
                str_builder += str(employee) + '\n'
            str_builder += '\t' +'}\n'
        
        str_builder += '}'
        return str_builder
    
    def save(self, indent='') -> str:
        str_builder = indent + f'DEPOT {self.name}' + ' {\n'
        
        for section in self.sections:
            str_builder += section.save(indent + '\t') + '\n'
        
        if len(self.employees) > 0:
            str_builder += indent + '\t' + 'EMPLOYEES {\n'
            for employee in self.employees:
                str_builder += employee.save(indent + '\t') + '\n'
            str_builder += indent + '\t' +'}\n'
        
        str_builder += indent + '}'
        return str_builder



class Section:
    def __init__(self):
        self.name = None
        self.products = []
        
    def __str__(self):
        str_builder = f'SECTION {self.name}' + ' {\n'
        
        for product in self.products:
            str_builder += str(product) + '\n'
            
        str_builder += '}'
        return str_builder
        
    def save(self, indent='') -> str:
        str_builder = indent + f'SECTION {self.name}' + ' {\n'
            
        for product in self.products:
            str_builder += product.save(indent + '\t') + '\n'
                
        str_builder += indent + '}'
        return str_builder
        


class Product:
    def __init__(self):
        self.name = None
        self.category = None
        self.quantity = None
        self.unit = None
        
    def __str__(self, ):
        return f'PRODUCT {self.name} ' + '{' + f'{self.category}, {self.quantity}, {self.unit}' + '}'
    
    def save(self, indent='') -> str:
        return indent + f'PRODUCT {self.name} ' + '{' + f'{self.category}, {self.quantity}, {self.unit}' + '}'



class Employee:
    def __init__(self):
        self.name = None
        self.surname = None
        self.office = None
        self.employment_date = None
        self.sections = []
        
    def __str__(self, ):
        str_builder = f'EMPLOYEE {self.name} {self.surname} ' + '{' + f'{self.office}, {self.employment_date}, SECTION '
        
        for i, section in enumerate(self.sections):
            if i != 0:
                str_builder += ', '
            str_builder += section
            
        str_builder += '}'
        return str_builder
    
    def save(self, indent='') -> str:
        str_builder = indent + f'EMPLOYEE {self.name} {self.surname} ' + '{' + f'{self.office}, {self.employment_date}, SECTION '
        
        for i, section in enumerate(self.sections):
            if i != 0:
                str_builder += ', '
            str_builder += section
            
        str_builder += '}'
        return str_builder
    

