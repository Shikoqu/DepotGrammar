# Generated from DepotParser.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .DepotParser import DepotParser
else:
    from DepotParser import DepotParser

# This class defines a complete listener for a parse tree produced by DepotParser.
class DepotParserListener(ParseTreeListener):

    # Enter a parse tree produced by DepotParser#program.
    def enterProgram(self, ctx:DepotParser.ProgramContext):
        pass

    # Exit a parse tree produced by DepotParser#program.
    def exitProgram(self, ctx:DepotParser.ProgramContext):
        pass


    # Enter a parse tree produced by DepotParser#depot.
    def enterDepot(self, ctx:DepotParser.DepotContext):
        pass

    # Exit a parse tree produced by DepotParser#depot.
    def exitDepot(self, ctx:DepotParser.DepotContext):
        pass


    # Enter a parse tree produced by DepotParser#depot_name.
    def enterDepot_name(self, ctx:DepotParser.Depot_nameContext):
        pass

    # Exit a parse tree produced by DepotParser#depot_name.
    def exitDepot_name(self, ctx:DepotParser.Depot_nameContext):
        pass


    # Enter a parse tree produced by DepotParser#depot_body.
    def enterDepot_body(self, ctx:DepotParser.Depot_bodyContext):
        pass

    # Exit a parse tree produced by DepotParser#depot_body.
    def exitDepot_body(self, ctx:DepotParser.Depot_bodyContext):
        pass


    # Enter a parse tree produced by DepotParser#section_list.
    def enterSection_list(self, ctx:DepotParser.Section_listContext):
        pass

    # Exit a parse tree produced by DepotParser#section_list.
    def exitSection_list(self, ctx:DepotParser.Section_listContext):
        pass


    # Enter a parse tree produced by DepotParser#section.
    def enterSection(self, ctx:DepotParser.SectionContext):
        pass

    # Exit a parse tree produced by DepotParser#section.
    def exitSection(self, ctx:DepotParser.SectionContext):
        pass


    # Enter a parse tree produced by DepotParser#section_name.
    def enterSection_name(self, ctx:DepotParser.Section_nameContext):
        pass

    # Exit a parse tree produced by DepotParser#section_name.
    def exitSection_name(self, ctx:DepotParser.Section_nameContext):
        pass


    # Enter a parse tree produced by DepotParser#section_body.
    def enterSection_body(self, ctx:DepotParser.Section_bodyContext):
        pass

    # Exit a parse tree produced by DepotParser#section_body.
    def exitSection_body(self, ctx:DepotParser.Section_bodyContext):
        pass


    # Enter a parse tree produced by DepotParser#product.
    def enterProduct(self, ctx:DepotParser.ProductContext):
        pass

    # Exit a parse tree produced by DepotParser#product.
    def exitProduct(self, ctx:DepotParser.ProductContext):
        pass


    # Enter a parse tree produced by DepotParser#product_name.
    def enterProduct_name(self, ctx:DepotParser.Product_nameContext):
        pass

    # Exit a parse tree produced by DepotParser#product_name.
    def exitProduct_name(self, ctx:DepotParser.Product_nameContext):
        pass


    # Enter a parse tree produced by DepotParser#product_body.
    def enterProduct_body(self, ctx:DepotParser.Product_bodyContext):
        pass

    # Exit a parse tree produced by DepotParser#product_body.
    def exitProduct_body(self, ctx:DepotParser.Product_bodyContext):
        pass


    # Enter a parse tree produced by DepotParser#category.
    def enterCategory(self, ctx:DepotParser.CategoryContext):
        pass

    # Exit a parse tree produced by DepotParser#category.
    def exitCategory(self, ctx:DepotParser.CategoryContext):
        pass


    # Enter a parse tree produced by DepotParser#category_name.
    def enterCategory_name(self, ctx:DepotParser.Category_nameContext):
        pass

    # Exit a parse tree produced by DepotParser#category_name.
    def exitCategory_name(self, ctx:DepotParser.Category_nameContext):
        pass


    # Enter a parse tree produced by DepotParser#quantity.
    def enterQuantity(self, ctx:DepotParser.QuantityContext):
        pass

    # Exit a parse tree produced by DepotParser#quantity.
    def exitQuantity(self, ctx:DepotParser.QuantityContext):
        pass


    # Enter a parse tree produced by DepotParser#unit.
    def enterUnit(self, ctx:DepotParser.UnitContext):
        pass

    # Exit a parse tree produced by DepotParser#unit.
    def exitUnit(self, ctx:DepotParser.UnitContext):
        pass


    # Enter a parse tree produced by DepotParser#unit_name.
    def enterUnit_name(self, ctx:DepotParser.Unit_nameContext):
        pass

    # Exit a parse tree produced by DepotParser#unit_name.
    def exitUnit_name(self, ctx:DepotParser.Unit_nameContext):
        pass


    # Enter a parse tree produced by DepotParser#employee_list.
    def enterEmployee_list(self, ctx:DepotParser.Employee_listContext):
        pass

    # Exit a parse tree produced by DepotParser#employee_list.
    def exitEmployee_list(self, ctx:DepotParser.Employee_listContext):
        pass


    # Enter a parse tree produced by DepotParser#employees_body.
    def enterEmployees_body(self, ctx:DepotParser.Employees_bodyContext):
        pass

    # Exit a parse tree produced by DepotParser#employees_body.
    def exitEmployees_body(self, ctx:DepotParser.Employees_bodyContext):
        pass


    # Enter a parse tree produced by DepotParser#employee.
    def enterEmployee(self, ctx:DepotParser.EmployeeContext):
        pass

    # Exit a parse tree produced by DepotParser#employee.
    def exitEmployee(self, ctx:DepotParser.EmployeeContext):
        pass


    # Enter a parse tree produced by DepotParser#employee_body.
    def enterEmployee_body(self, ctx:DepotParser.Employee_bodyContext):
        pass

    # Exit a parse tree produced by DepotParser#employee_body.
    def exitEmployee_body(self, ctx:DepotParser.Employee_bodyContext):
        pass


    # Enter a parse tree produced by DepotParser#employee_sections.
    def enterEmployee_sections(self, ctx:DepotParser.Employee_sectionsContext):
        pass

    # Exit a parse tree produced by DepotParser#employee_sections.
    def exitEmployee_sections(self, ctx:DepotParser.Employee_sectionsContext):
        pass


    # Enter a parse tree produced by DepotParser#name.
    def enterName(self, ctx:DepotParser.NameContext):
        pass

    # Exit a parse tree produced by DepotParser#name.
    def exitName(self, ctx:DepotParser.NameContext):
        pass


    # Enter a parse tree produced by DepotParser#surname.
    def enterSurname(self, ctx:DepotParser.SurnameContext):
        pass

    # Exit a parse tree produced by DepotParser#surname.
    def exitSurname(self, ctx:DepotParser.SurnameContext):
        pass


    # Enter a parse tree produced by DepotParser#office.
    def enterOffice(self, ctx:DepotParser.OfficeContext):
        pass

    # Exit a parse tree produced by DepotParser#office.
    def exitOffice(self, ctx:DepotParser.OfficeContext):
        pass


    # Enter a parse tree produced by DepotParser#employment_date.
    def enterEmployment_date(self, ctx:DepotParser.Employment_dateContext):
        pass

    # Exit a parse tree produced by DepotParser#employment_date.
    def exitEmployment_date(self, ctx:DepotParser.Employment_dateContext):
        pass



del DepotParser