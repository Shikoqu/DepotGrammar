from typing import Optional

from .unit import Unit
from .employee_list import EmployeeList
from .section_list import SectionList


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
        self.sections.normalize()
        self.employees.normalize()
    
    def merge(self, other: 'Depot'):
        if self is other:
            return
        self.sections.add_all(other.sections)
        self.employees.add_all(other.employees)
        self.normalize()
        
    
    def __str__(self, indent='') -> str:
        str_builder = indent + f'DEPOT {self.name}' + ' {\n'
        
        for section in self.sections:
            str_builder += section.__str__(indent + '\t') + '\n'
        
        if len(self.employees) > 0:
            str_builder += indent + '\t' + 'EMPLOYEES {\n'
            for employee in self.employees:
                str_builder += employee.__str__(indent + '\t\t') + '\n'
            str_builder += indent + '\t}\n'
        
        str_builder += indent + '}'
        return str_builder
    
