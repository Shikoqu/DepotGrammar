from .unit_list import UnitList


class EmployeeList(UnitList):
    def filter(self, filter):
        raise NotImplementedError()
    
    def sort(self, key):
        raise NotImplementedError()

