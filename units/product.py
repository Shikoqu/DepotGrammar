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

