# from abc import ABC, abstractmethod
from typing import List, Optional

from .unit import Unit


class UnitList:
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
    
    
    def find(self, key) -> Unit | None:
        return next((u for u in self.data if u.key == key), None)
    
    def sort_inplace(self, key):
        self.data.sort(key=key)
        return self
    
    def __iter__(self):
        return iter(self.data)
    
    def __len__(self):
        return len(self.data)
    
    def filter(self, filter) -> 'UnitList | None':
        unit_list = UnitList()
        for d in self.data:
            if filter(d):
                unit_list.data.append(d)
        if len(unit_list) == 0:
            return None
        return unit_list
    
    def sort(self, key) -> 'UnitList':
        return UnitList(sorted(self.data, key=key))
    