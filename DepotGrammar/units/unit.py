from abc import ABC, abstractmethod


class Unit(ABC):
    def __init__(self, name: str):
        """Initializes a unit.
        """
        self.name: str = name
        
    @property
    def key(self):
        """Key used to tell units apart.
        
        Units with the same key are considered equal.
        """
        pass
    
    @abstractmethod
    def normalize(self):
        """Normalizes the unit.
        """
        pass
    
    @abstractmethod
    def merge(self, other):
        """Merges two units.
        
        Checks if merges with itself to avoid recursion.
        """
        pass
    
    
    @abstractmethod
    def __str__(self, indent=''):
        """Returns a string representation of the unit compatible with depot grammar.
        """
        pass
    
