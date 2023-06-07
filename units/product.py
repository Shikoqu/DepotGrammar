from enum import Enum


class Product:
    """Class representing a product.
    """
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
        """Initializes a product.
        
        Args:
            - name (str, optional): name of the product. Defaults to None.
            - category (str, optional): category of the product. Defaults to None.
            - quantity (int, optional): quantity of the product. Defaults to None.
            - unit (Unit, optional): unit of the quantity (pc/kg/l//m/m2/m3). Defaults to None.
        """
        self.name: str = name
        self.category: str = category
        self.quantity: int = quantity
        self.unit: Product.Unit = unit
        
    def normalize(self):
        """Normalizes the product.
        
        Converts the quantity to int and the unit to Product.Unit enum.
        Assumes that quantity is a number and unit is in correct format (pc/kg/l/m/m2/m3).
        """
        if type(self.quantity) is not int:
            self.quantity = int(self.quantity)
        if type(self.unit) is not Product.Unit:
            self.unit = Product.Unit(self.unit)
        
        
    def __str__(self, indent='') -> str:
        return indent + f'PRODUCT {self.name} ' + '{' + f'{self.category}, {self.quantity}, {self.unit}' + '}'

