from typing import List, Optional

from .unit import Unit
from .product import Product
from .product_list import ProductList


class Section(Unit):
    def __init__(self,
                 name: str = None,
                 products: Optional[ProductList] = None):
        """Initializes a section.

        Args:
            - name (str): name of the section. Defaults to None.
            - products (Optional[ProductList]): products in the section. Defaults to None.
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
        
    
    def contains_any(self, products: List[Product], product_filter = None) -> bool:
        """Check if the section contains any of the products.

        Args:
            - products (List[Product]): List of products to check
            - product_filter (lambda exp): Tells what atributes to look for in products. Defaults to None.
            
        if product_filter is None:
        checks products by their key

        Returns:
            - bool: True if the section contains any of the products, False otherwise.
        """
        for product in products:
            if self.contains(product, product_filter):
                return True
        return False
    
    def contains_all(self, products: List[Product], product_filter = None) -> bool:
        """Check if the section contains all of the products.

        Args:
            - products (List[Product]): List of products to check
            - product_filter (lambda exp): Tells what atributes to look for in products. Defaults to None.
            
        if product_filter is None:
        checks products by their key

        Returns:
            - bool: True if the section contains all of the products, False otherwise.
        """
        for product in products:
            if not self.contains(product, product_filter):
                return False
        return True
    
    def contains(self, product: Product, product_filter = None) -> bool:
        """Check if the section contains the product.

        Args:
            - product (Product): Product to check
            - product_filter (lambda exp): Tells what atributes to look for in products. Defaults to None.
            
        if product_filter is None:
        checks products by their key

        Returns:
            - bool: True if the section contains the product, False otherwise.
        """
        if product_filter is not None:
            if self.products.filter(filter=lambda p: product_filter(p) == product_filter(product)) is not None:
                return True
        else: # product_filter is None
            if self.products.find(product.key) is not None:
                return True
        return False
    
        
    def __str__(self, indent='') -> str:
        str_builder = indent + f'SECTION {self.name}' + ' {\n'
            
        for product in self.products:
            str_builder += product.__str__(indent + '\t') + '\n'
                
        str_builder += indent + '}'
        return str_builder
        
        
