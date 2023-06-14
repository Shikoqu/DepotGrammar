from typing import List

from .product import Product
from .unit_list import UnitList


class SectionList(UnitList):
    def contains_any(self, products: List[Product], product_filter = None) -> bool:
        """Check if the sections contains any of the products.

        Args:
            - products (List[Product]): List of products to check
            - product_filter (lambda exp): Tells what atributes to look for in products. Defaults to None.
            
        if product_filter is None:
        checks products by their key

        Returns:
            - bool: True if any of the sections contains any of the products, False otherwise.
        """
        if self.filter(lambda s: s.contains_any(products, product_filter)) is not None:
            return True
        return False
    
    def contains_all(self, products: List[Product], product_filter = None) -> bool:
        """Check if the sections contains all of the products.

        Args:
            products (List[Product]): List of products to check
            product_filter (lambda exp): Tells what atributes to look for in products. Defaults to None.
            
        if product_filter is None:
        checks products by their key

        Returns:
            bool: True if the sections contains all of the products, False otherwise.
        """
        for product in products:
            if not self.contains(product, product_filter):
                return False
        return True
    
    def contains(self, product: Product, product_filter = None) -> bool:
        """Check if the sections contains the product.

        Args:
            - product (Product): Product to check
            - product_filter (lambda exp): Tells what atributes to look for in products. Defaults to None.
            
        if product_filter is None:
        checks products by their key

        Returns:
            - bool: True if any of the sections contains the product, False otherwise.
        """
        if self.filter(lambda s: s.contains(product, product_filter)) is not None:
            return True
        return False
    
    