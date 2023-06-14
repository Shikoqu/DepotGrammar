from antlr4 import *
from .grammar import DepotLexer, DepotParser, DepotListener

from .units.depot import Depot


def read(filename: str) -> Depot:
    with open(filename, 'r') as file:
        code = file.read()
        parser = parse(code)
        tree = parser.program()
        
        listener = DepotListener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        
        return listener.depot

def parse(code: str) -> DepotParser:
    input_stream = InputStream(code)

    lexer = DepotLexer(input_stream)
    token_stream = CommonTokenStream(lexer)

    return DepotParser(token_stream)

def save(depot: Depot, filename: str):
    with open(filename, 'w') as f:
        f.write(depot.__str__())