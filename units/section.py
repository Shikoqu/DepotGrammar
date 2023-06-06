from typing import List, Optional

from .product import Product


class Section:
    def __init__(self,
                 name: str = None,
                 products: Optional[List[Product]] = []):
        self.name: str = name
        self.products: List[Product] = products or []
        
    def normalize(self):
        products_norm = {}
        for product in self.products:
            if (product.name, product.category) in products_norm:
                products_norm[(product.name, product.category)].quantity += product.quantity
            else:
                products_norm[(product.name, product.category)] = product
        self.products = list(products_norm.values())
        
        for product in self.products:
            product.normalize()
    

    
    def add_product(self, product):
        self.products.append(product)
        
        
    def contains_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                return True
        return False
    
    def count_product(self, product_name):
        count = 0
        for product in self.products:
            if product.name == product_name:
                count += product.quantity
        return count
    
    def find_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                return product
        return None
    
    def remove_product(self, product_name, quantity=0):
        NotImplementedError
    
        
    def __str__(self, indent='') -> str:
        str_builder = indent + f'SECTION {self.name}' + ' {\n'
            
        for product in self.products:
            str_builder += product.__str__(indent + '\t') + '\n'
                
        str_builder += indent + '}'
        return str_builder
        
    def save(self, indent='') -> str:
        str_builder = indent + f'SECTION {self.name}' + ' {\n'
            
        for product in self.products:
            str_builder += product.save(indent + '\t') + '\n'
                
        str_builder += indent + '}'
        return str_builder
        
