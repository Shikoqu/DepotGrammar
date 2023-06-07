from typing import List, Optional

from .product import Product


class Section:
    def __init__(self,
                 name: str = None,
                 products: Optional[List[Product]] = None):
        """Initializes a section.

        Args:
            - name (str, optional): name of the section. Defaults to None.
            - products (Optional[List[Product]], optional): products in the section. Defaults to None.
        """
        self.name: str = name
        self.products: List[Product] = products or []
        
    def normalize(self):
        """Normalizes the section.
        
        Products with the same name and category are merged.
        """
        products_norm = {}
        for product in self.products:
            if (product.name, product.category) in products_norm:
                products_norm[(product.name, product.category)].quantity += product.quantity
            else:
                products_norm[(product.name, product.category)] = product
        self.products = list(products_norm.values())
        
        for product in self.products:
            product.normalize()
    
    
    def __iadd__(self, unit):
        """Adds unit to the section regarding unit type.
        
        - If unit is Product, adds it to the section.
        - If unit is Section, its merged to the section.
        - If unit is List, adds all units from list to the section.
        
        Args:
            - unit (Product, Section, list of Products, list of Sections): to be added to the section.
            
        Raises:
            - TypeError: if unit is not Product, Section, list of Products or Sections.
        """
        if isinstance(unit, Product):
            self.add_product(unit)
        elif isinstance(unit, Section):
            self.merge_section(unit)
        elif isinstance(unit, list):
            for u in unit:
                self.__iadd__(u)
        else:
            raise TypeError(f'Cannot add {type(unit)} to Section')
    
    def add_product(self, product: Product):
        """Adds a product to the section.

        Args:
            - product (Product): Product to be added.
        """
        self.products.append(product)

    def merge_section(self, section: Section):
        """Merge section with the section.
        
        The list of products is extended by the list of products from the section and then normalized.
        """
        self.products.extend(section.products)
        self.normalize()
        
        
    def contains_product(self, product_name: str) -> bool:
        """
        Checks if the section contains a product with the given name.

        Args:
            product_name (str): Name of the product to be checked.

        Returns:
            bool: True if the section contains a product with the given name, False otherwise.
        """
        for product in self.products:
            if product.name == product_name:
                return True
        return False
    
    def count_product(self, product_name: str):
        """Counts the number of products with the given name in the section.

        Args:
            product_name (_type_): _description_

        Returns:
            _type_: _description_
        """
        count = 0
        for product in self.products:
            if product.name == product_name:
                count += product.quantity
        return count
    
    def find_product(self, product_name):
        """Returns a product with the given name and category in the section.
        """
        for product in self.products:
            if product.name == product_name:
                return product
        return None
    
    def remove_product(self, product_name, quantity=0):
        """Removes a product with the given name and category from the section.
        """
        raise NotImplementedError
    
        
    def __str__(self, indent='') -> str:
        str_builder = indent + f'SECTION {self.name}' + ' {\n'
            
        for product in self.products:
            str_builder += product.__str__(indent + '\t') + '\n'
                
        str_builder += indent + '}'
        return str_builder
        
        
