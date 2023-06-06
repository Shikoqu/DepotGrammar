from datetime import date, datetime
from typing import List, Optional

from .section import Section


class Employee:
    def __init__(self,
                 name: str = None,
                 surname: str = None,
                 office: str = None,
                 employment_date: date = None,
                 sections: Optional[List[Section]] = None):
        self.name: str = name
        self.surname: str = surname
        self.office: str = office
        self.employment_date: date = employment_date
        self.sections: List[Section] = sections or []
        
    def normalize(self, sections: List[Section]):
        if self.employment_date is not date:
            self.employment_date = datetime.strptime(self.employment_date, '%d/%m/%Y').date()
            
        section_dict = {section.name: section for section in sections}
        self.sections = [section_dict.get(section, Section('dupa')) for section in self.sections]
    
    
    def add_section(self, section):
        self.sections.append(section)
        
    
    def find_product(self, product_name):
        sections = []
        product = None
        
        for section in self.sections:
            for product in section.products:
                if product.name == product_name:
                    sections.append(section)
        
        if product is not None:
            return product, sections
        return None
    
        
    def __str__(self, indent='') -> str:
        str_builder = indent + f'EMPLOYEE {self.name} {self.surname} ' + '{' + f'{self.office}, {self.employment_date.strftime("%d/%m/%Y")}, SECTION '
        
        for i, section in enumerate(self.sections):
            if i != 0:
                str_builder += ', '
            str_builder += section.name
            
        str_builder += '}'
        return str_builder
    
    def save(self, indent='') -> str:
        str_builder = indent + f'EMPLOYEE {self.name} {self.surname} ' + '{' + f'{self.office}, {self.employment_date.strftime("%d/%m/%Y")}, SECTION '
        
        for i, section in enumerate(self.sections):
            if i != 0:
                str_builder += ', '
            str_builder += section.name
            
        str_builder += '}'
        return str_builder
    

