from .unit_list import UnitList


class SectionList(UnitList):
    def filter(self, filter):
        raise NotImplementedError()
    
    def sort(self, key):
        raise NotImplementedError()
    
    
    