from antlr4 import *
from grammar.DepotParser import DepotParser
from grammar.DepotParserListener import DepotParserListener
from Units import *

# This class defines a complete listener for a parse tree produced by DepotParser.
class DepotListener(DepotParserListener):
    def __init__(self):
        self.current_depot = None
        self.current_section = None
        self.current_product = None
        self.current_employee = None
        
        self.data = None
        


    def enterDepot(self, ctx:DepotParser.DepotContext):
        self.current_depot = Depot()

    def exitDepot(self, ctx:DepotParser.DepotContext):
        self.data = self.current_depot
        # self.current_depot = None


    def enterDepot_name(self, ctx:DepotParser.Depot_nameContext):
        self.current_depot.name = ctx.getText()



    def enterSection(self, ctx:DepotParser.SectionContext):
        self.current_section = Section()

    def exitSection(self, ctx:DepotParser.SectionContext):
        self.current_depot.sections.append(self.current_section)
        # self.current_section = None


    def enterSection_name(self, ctx:DepotParser.Section_nameContext):
        self.current_section.name = ctx.getText()



    def enterProduct(self, ctx:DepotParser.ProductContext):
        self.current_product = Product()

    def exitProduct(self, ctx:DepotParser.ProductContext):
        self.current_section.products.append(self.current_product)
        # self.current_product = None


    def enterProduct_name(self, ctx:DepotParser.Product_nameContext):
        self.current_product.name = ctx.getText()

    def enterCategory_name(self, ctx:DepotParser.Category_nameContext):
        self.current_product.category = ctx.getText()

    def enterQuantity(self, ctx:DepotParser.QuantityContext):
        self.current_product.quantity = int(ctx.getText())

    def enterUnit_name(self, ctx:DepotParser.Unit_nameContext):
        self.current_product.unit = ctx.getText()



    def enterEmployee(self, ctx:DepotParser.EmployeeContext):
        self.current_employee = Employee()

    def exitEmployee(self, ctx:DepotParser.EmployeeContext):
        self.current_depot.employees.append(self.current_employee)
        # self.current_employee = None


    def enterName(self, ctx:DepotParser.NameContext):
        self.current_employee.name = ctx.getText()

    def enterSurname(self, ctx:DepotParser.SurnameContext):
        self.current_employee.surname = ctx.getText()

    def enterOffice(self, ctx:DepotParser.OfficeContext):
        self.current_employee.office = ctx.getText()

    def enterEmployment_date(self, ctx:DepotParser.Employment_dateContext):
        self.current_employee.employment_date = ctx.getText()

    def enterEmployee_sections(self, ctx:DepotParser.Employee_sectionsContext):
        self.current_employee.sections = [name.getText() for name in ctx.section_name()]
