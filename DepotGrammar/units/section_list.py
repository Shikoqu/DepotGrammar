from typing import List

from .product import Product
from .unit_list import UnitList


class SectionList(UnitList):
    def contains_any(self, products: List[Product], product_filter = None) -> bool:
        if self.filter(lambda s: s.contains_any(products, product_filter)) is not None:
            return True
        return False
    
    def contains_all(self, products: List[Product], product_filter = None) -> bool:
        for product in products:
            if not self.contains(product, product_filter):
                return False
        return True
    
    def contains(self, product: Product, product_filter = None) -> bool:
        if self.filter(lambda s: s.contains(product, product_filter)) is not None:
            return True
        return False
    
    