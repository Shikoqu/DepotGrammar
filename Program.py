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


# Przejście przez drzewo rozbioru i przetwarzanie
def traverse_tree(node, indent=''):
    if isinstance(node, TerminalNode):
        print(indent + node.getText())
    else:
        for child in node.getChildren():
            traverse_tree(child, indent + '  ')


def main():
    code = open('example.txt').read()

    parser = parse(code)
    tree = parser.program()

    # Utwórz instancję listenera
    listener = DepotListener()

    # Przechodź przez drzewo rozbioru i wywołuj metody listenera
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    my_depot = listener.data

    print('done')
    print(my_depot.__str__(indent='|'))


if __name__ == '__main__':
    main()