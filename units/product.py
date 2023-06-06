from enum import Enum


class Product:
    class Unit(Enum):
        PIECE = 'pc'
        KILOGRAM = 'kg'
        LITER = 'l'
        METER = 'm'
        SQUARE_METER = 'm2'
        CUBIC_METER = 'm3'

    def __init__(self,
                 name: str = None,
                 category: str = None,
                 quantity: int = None,
                 unit: Unit = None):
        self.name: str = name
        self.category: str = category
        self.quantity: int = quantity
        self.unit: Product.Unit = unit
        
    def normalize(self):
        if type(self.quantity) is not int:
            self.quantity = int(self.quantity)
        if type(self.unit) is not Product.Unit:
            self.unit = Product.Unit(self.unit)
        
    def __str__(self, indent='') -> str:
        return indent + f'PRODUCT {self.name} ' + '{' + f'{self.category}, {self.quantity}, {self.unit}' + '}'
    
    def save(self, indent='') -> str:
        return indent + f'PRODUCT {self.name} ' + '{' + f'{self.category}, {self.quantity}, {self.unit.value}' + '}'

