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
        
