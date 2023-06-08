from abc import ABC, abstractmethod


class Unit(ABC):
    def __init__(self, name: str):
        self.name: str = name
        
    @property
    def key(self):
        pass
    
    @abstractmethod
    def normalize(self):
        pass
    
    @abstractmethod
    def merge(self, other):
        pass
    
    
    @abstractmethod
    def __str__(self, indent=''):
        pass
    
