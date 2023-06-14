from typing import List, Optional

from .unit import Unit


class UnitList:
    def __init__(self, data: Optional[List] = None):
        self.data: List = data or []
        
    @property
    def keys(self):
        """Key used to tell units apart.
        
        Units with the same key are considered equal.
        
        Returns:
            - Returns a list of keys of the units in the list.
        """
        return [d.key for d in self.data]
    
    def normalize(self):
        """Normalizes the unit list.
        
        Removes duplicates and merges units with the same key.
        Then normalizes each unit.
        """
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
        """Adds a unit to the list.
        """
        if unit.key not in self.keys:
            self.data.append(unit)
        else:
            this_unit = self.find(unit.key)
            this_unit.merge(unit)
    
    def add_all(self, units: 'UnitList'):
        """Adds all units from another unit list.
        """
        for unit in units.data:
            self.add(unit)
    
    
    def find(self, key) -> Unit:
        """Finds a unit with a given key.
        
        Assumes that there is only one unit with the given key.

        Args:
            - key: The key of the unit to find.

        Returns:
            - Unit: Returns the unit with the given key or None if not found.
        """
        return next((u for u in self.data if u.key == key), None)
    
    def sort_inplace(self, key) -> 'UnitList':
        """Sorts the unit list in place.

        Args:
            - key (lambda exp): The key to sort by.

        Returns:
            - self
        """
        self.data.sort(key=key)
        return self
    
    def __iter__(self):
        """Iterates over the units in the list.
        
        Implements Iterator Protocol - allows to iterate over the unit list.
        
        ```
            for unit in unit_list:
                ...
        ```
        instead of
        ```
            for unit in unit_list.data:
                ...
        ```
        
        """
        return iter(self.data)
    
    def __len__(self):
        """Returns the number of units in the list.
        
        Implements the len() function.
        
        ```
            len(unit_list)
        ```
        instead of
        ```
            len(unit_list.data)
        ```
        """
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
    
