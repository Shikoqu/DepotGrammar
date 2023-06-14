from datetime import datetime
from antlr4 import *

from .DepotParser import DepotParser
from ..units import Depot, Section, Product, Employee


class DepotListener(ParseTreeListener):
    """This class defines a listener for a parse tree produced by DepotParser.
    
    Produces and initializes a depot object with all its contents from a parse tree.
    
    Attributes:
        - current_depot (Depot): Depot currently being parsed.
        - current_section (Section): Section currently being parsed.
        - current_product (Product): Product currently being parsed.
        - current_employee (Employee): Employee currently being parsed.
        - #### depot (Depot): Depot object produced by the listener.
    """
    def __init__(self):
        self.current_depot: Depot = None
        self.current_section: Section = None
        self.current_product: Product = None
        self.current_employee: Employee = None
        
        self.depot: Depot = None
        
    # DEPOT
    def enterDepot(self, ctx:DepotParser.DepotContext):
        self.current_depot = Depot()

    def exitDepot(self, ctx:DepotParser.DepotContext):
        self.depot = self.current_depot
        self.current_depot = None

    def enterDepot_name(self, ctx:DepotParser.Depot_nameContext):
        self.current_depot.name = ctx.getText()


    # SECTION
    def enterSection(self, ctx:DepotParser.SectionContext):
        self.current_section = Section()

    def exitSection(self, ctx:DepotParser.SectionContext):
        self.current_depot.sections.add(self.current_section)
        self.current_section = None

    def enterSection_name(self, ctx:DepotParser.Section_nameContext):
        self.current_section.name = ctx.getText()


    # PRODUCT
    def enterProduct(self, ctx:DepotParser.ProductContext):
        self.current_product = Product()

    def exitProduct(self, ctx:DepotParser.ProductContext):
        self.current_section.products.add(self.current_product)
        self.current_product = None

    def enterProduct_name(self, ctx:DepotParser.Product_nameContext):
        self.current_product.name = ctx.getText()

    def enterCategory_name(self, ctx:DepotParser.Category_nameContext):
        self.current_product.category = ctx.getText()

    def enterQuantity(self, ctx:DepotParser.QuantityContext):
        self.current_product.quantity = int(ctx.getText())

    def enterUnit_name(self, ctx:DepotParser.Unit_nameContext):
        self.current_product.unit = Product.Punit(ctx.getText())


    # EMPLOYEE
    def enterEmployee(self, ctx:DepotParser.EmployeeContext):
        self.current_employee = Employee(self.current_depot)

    def exitEmployee(self, ctx:DepotParser.EmployeeContext):
        self.current_depot.employees.add(self.current_employee)
        self.current_employee = None

    def enterName(self, ctx:DepotParser.NameContext):
        self.current_employee.name = ctx.getText()

    def enterSurname(self, ctx:DepotParser.SurnameContext):
        self.current_employee.surname = ctx.getText()

    def enterOffice(self, ctx:DepotParser.OfficeContext):
        self.current_employee.office = ctx.getText()

    def enterEmployment_date(self, ctx:DepotParser.Employment_dateContext):
        self.current_employee.employment_date = datetime.strptime(ctx.getText(), '%d/%m/%Y').date()
    
    def enterEmployee_section_name(self, ctx:DepotParser.Employee_section_nameContext):
        self.current_employee.add_section(ctx.getText())
            
