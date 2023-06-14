from enum import Enum

from .unit import Unit


class Product(Unit):
    """Class representing a product.
    """
    class Punit(Enum):
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
                 unit: Punit = None):
        """Initializes a product.
        
        Args:
            - name (str): name of the product. Defaults to None.
            - category (str): category of the product. Defaults to None.
            - quantity (int): quantity of the product. Defaults to None.
            - unit (Unit): unit of the quantity (pc/kg/l//m/m2/m3). Defaults to None.
        """
        super().__init__(name)
        self.category: str = category
        self.quantity: int = quantity
        self.unit: Product.Punit = unit
        
    @property
    def key(self):
        return (self.name, self.category)
    
    def normalize(self):
        pass
            
    def merge(self, other: 'Product'):
        if self is other:
            return
        self.quantity += other.quantity
        

    def __str__(self, indent='') -> str:
        return indent + f'PRODUCT {self.name} ' + '{' + f'{self.category}, {self.quantity}, {self.unit}' + '}'

