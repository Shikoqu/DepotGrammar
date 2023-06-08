from datetime import date, datetime
from typing import Optional

from .depot import Depot
from .unit import Unit
from .section import Section
from .section_list import SectionList


class Employee(Unit):
    """class representing an employee.
    """
    def __init__(self,
                 depot: Depot,
                 name: str = None,
                 surname: str = None,
                 office: str = None,
                 employment_date: date = None,
                 sections: Optional[SectionList] = None):
        """Initializes an employee.
        
        Args:
            - name (str, optional): Defaults to None.
            - surname (str, optional): Defaults to None.
            - office (str, optional): Defaults to None.
            - employment_date (date, optional): format - %d/%m/%Y. Defaults to None.
            - sections (Optional[List[Section]], optional): Section must be already in depot. Defaults to None.
        """
        self.depot: Depot = depot
        super().__init__(name)
        self.surname: str = surname
        self.office: str = office
        self.employment_date: date = employment_date
        self.sections: SectionList = sections or SectionList()
        
    @property
    def key(self):
        return (self.name, self.surname)
    
    def add_section(self, section_name: str):
        if section_name not in self.sections.keys:
            self.sections.add(self.depot.sections.find(section_name))
    
    def normalize(self):
        pass
        
    def merge(self, other: 'Employee'):
        if self is other:
            return
        self.sections.add_all(other.sections)
    
        
    def __str__(self, indent='') -> str:
        str_builder = indent + f'EMPLOYEE {self.name} {self.surname} ' + '{' + f'{self.office}, {self.employment_date.strftime("%d/%m/%Y")}, SECTION '
        
        for i, section in enumerate(self.sections):
            if i != 0:
                str_builder += ', '
            str_builder += section.name
            
        str_builder += '}'
        return str_builder
    
    

