from abc import ABC, abstractmethod
from typing import List, Optional

from .unit import Unit


class UnitList(ABC):
    def __init__(self, data: Optional[List] = None):
        self.data: List = data or []
        
    @property
    def keys(self):
        return [d.key for d in self.data]
    
    def normalize(self):
        norm = {}
        for unit in self.data:
            if unit.key not in norm:
                norm[unit.key] = unit
            else:
                norm[unit.key].merge(unit)
        for unit in self.data:
            unit.normalize()
        self.data = list(norm.values())

    def add(self, unit: Unit):
        if unit.key not in self.keys:
            self.data.append(unit)
        else:
            this_unit = self.find(unit.key)
            this_unit.merge(unit)
    
    def add_all(self, units: 'UnitList'):
        for unit in units.data:
            self.add(unit)
    
    
    def find(self, key) -> Unit:
        return next((d for d in self.data if d.key == key), None)
    
    def sort_inplace(self, key):
        self.data.sort(key=key)
        return self
    
    def __iter__(self):
        return iter(self.data)
    
    def __len__(self):
        return len(self.data)
    
    @abstractmethod
    def filter(self, filter):
        # unit_list = UnitList()
        # for d in self.data:
        #     if filter(d):
        #         unit_list.units.append(d)
        # return unit_list
        pass
    
    def filter_inplace(self, filter):
        self.units = self.filter(filter).units
        return self
    
    @abstractmethod
    def sort(self, key):
        pass
    