import pprint

from domain.pif import ProgramInternalForm
from domain.scanner import *
from domain.symbol_table import SymbolTable
from myparser.grammar import Grammar
from myparser.parser import ParserRecursiveDescent


class Main:

    def __init__(self):
        self.st = SymbolTable(20)
        self.pif = ProgramInternalForm()
        self.scanner = Scanner()

    def run(self, file_name):
        """
        Parses a file
        :param file_name: File to parse
        """
        readFile()
        exception_message = ""

        with open(file_name, 'r') as file:
            for lineCounter, line in enumerate(file, start=1):
                tokens = self.scanner.tokenize(line.rstrip())
                extra = ''
                for i in range(len(tokens)):
                    if tokens[i] in reservedWords + separators + operators:
                        if tokens[i] == ' ':  # ignore adding spaces to the pif
                            continue
                        self.pif.add(tokens[i], (-1, -1))
                    elif self.scanner.isIdentifier(tokens[i]):
                        identif = self.st.add(tokens[i])
                        self.pif.add("identifier", identif)
                    elif self.scanner.isConstant(tokens[i]):
                        const = self.st.add(extra + tokens[i])
                        extra = ''
                        self.pif.add("constant", const)
                    else:
                        exception_message += 'Lexical error at token ' + tokens[i] + ', at line ' + str(
                            lineCounter) + "\n"
                # self.pif.add("\n", (-1, -1))

        with open('st.out', 'w') as writer:
            writer.write(str(self.st))

        with open('pif.out', 'w') as writer:
            writer.write(str(self.pif))

        if exception_message == '':
            print("Lexically correct")
        else:
            print(exception_message)


if __name__ == "__main__":
    main = Main()
    main.run("p1.txt")
    with open("grammar.debug.txt", "w") as f:
        f.seek(0)
        pp = pprint.PrettyPrinter(indent=2, stream=f)
        gram = Grammar.parseFile("g2.txt")
        pp.pprint(gram.getNonTerminals())
        pp.pprint(gram.getTerminals())
        pp.pprint(gram.getStartingSymbol())
        pp.pprint(gram.getProductions())
        sequence = []
        for e in main.pif.get_content():
            sequence.append(str(e[0]))
        parser = ParserRecursiveDescent(gram)
        parser.run(sequence)
        parser.parse_tree(parser.work)
        parser.write_tree_to_file("g2")
