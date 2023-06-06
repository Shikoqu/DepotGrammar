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
    
