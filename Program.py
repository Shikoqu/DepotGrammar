from antlr4 import *

from DepotListener import DepotListener
from grammar import DepotLexer, DepotParser

def parse(code: str) -> DepotParser:
    # Utwórz strumień wejściowy dla analizy składniowej
    input_stream = InputStream(code)

    # Utwórz lekser
    lexer = DepotLexer(input_stream)
    token_stream = CommonTokenStream(lexer)

    # Utwórz parser
    parser = DepotParser(token_stream)
    
    return parser


def main():
    code = open('example.txt').read()

    parser = parse(code)
    tree = parser.program()

    # Utwórz instancję listenera
    listener = DepotListener()

    # Przechodź przez drzewo rozbioru i wywołuj metody listenera
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    my_depot = listener.depot

    print('done')
    print(my_depot)


if __name__ == '__main__':
    main()