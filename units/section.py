from typing import Optional

from .unit import Unit
from .product_list import ProductList


class Section(Unit):
    def __init__(self,
                 name: str = None,
                 products: Optional[ProductList] = None):
        """Initializes a section.

        Args:
            - name (str, optional): name of the section. Defaults to None.
            - products (Optional[ProductList], optional): products in the section. Defaults to None.
        """
        super().__init__(name)
        self.products: ProductList = products or ProductList()
        
    @property
    def key(self):
        return self.name
        
    def normalize(self):
        self.products.normalize()

    def merge(self, other: 'Section'):
        """Merge section with the section.
        
        The list of products is extended by the list of products from the section and then normalized.
        """
        if self is other:
            return
        self.products.add_all(other.products)
        self.normalize()
    
        
    def __str__(self, indent='') -> str:
        str_builder = indent + f'SECTION {self.name}' + ' {\n'
            
        for product in self.products:
            str_builder += product.__str__(indent + '\t') + '\n'
                
        str_builder += indent + '}'
        return str_builder
        
        
