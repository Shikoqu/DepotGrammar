from datetime import date, datetime
from typing import List, Optional

from .section import Section


class Employee:
    """class representing an employee.
    """
    def __init__(self,
                 name: str = None,
                 surname: str = None,
                 office: str = None,
                 employment_date: date = None,
                 sections: Optional[List[Section]] = None):
        """Initializes an employee.
        
        Args:
            - name (str, optional): Defaults to None.
            - surname (str, optional): Defaults to None.
            - office (str, optional): Defaults to None.
            - employment_date (date, optional): format - %d/%m/%Y. Defaults to None.
            - sections (Optional[List[Section]], optional): Section must be already in depot. Defaults to None.
        """
        self.name: str = name
        self.surname: str = surname
        self.office: str = office
        self.employment_date: date = employment_date
        self.sections: List[Section] = sections or []
        
    def normalize(self, sections: List[Section]):
        """Normalizes the employee.
        
        Converts the employment_date to date and the sections to Section objects.
        """
        if self.employment_date is not date:
            self.employment_date = datetime.strptime(self.employment_date, '%d/%m/%Y').date()
            
        section_dict = {section.name: section for section in sections}
        self.sections = [section_dict.get(section, Section(section)) for section in self.sections if isinstance(section, str)]
        
    
    def __iadd__(self, unit):
        """Adds unit to employee sections regarding unit type.
        
        If unit is Section, adds it to employee sections.
        If unit is List, adds all units from list to employee sections.

        Args:
            unit (Section, list of Sections): to be added to employee sections.

        Raises:
            TypeError: _description_
        """
        if isinstance(unit, Section):
            self.add_section(unit)
        elif isinstance(unit, List[Section]):
            self.sections.extend(unit)
        else:
            raise TypeError(f'Cannot add {unit} to Employee')
        return self
    
    def add_section(self, section: Section):
        """Adds section to employee sections.
        
        If section is just str you must call normalize() afterwards.
        Assumes that section is already in depot and employments_date is in correct format (%d/%m/%Y).
        """
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
    
    

