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
    

