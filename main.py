from domain.pif import ProgramInternalForm
from domain.scanner import *
from domain.symbol_table import SymbolTable


class Main:

    def __init__(self):
        self.st = SymbolTable(20)
        self.pif = ProgramInternalForm()
        self.scanner = Scanner()

    def run(self):
        readFile()
        file_name = "p1.txt"
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
                        self.pif.add("id", identif)
                    elif self.scanner.isConstant(tokens[i]):
                        const = self.st.add(extra + tokens[i])
                        extra = ''
                        self.pif.add("const", const)
                    else:
                        exception_message += 'Lexical error at token ' + tokens[i] + ', at line ' + str(
                            lineCounter) + "\n"

        with open('st.out', 'w') as writer:
            writer.write(str(self.st))

        with open('pif.out', 'w') as writer:
            writer.write(str(self.pif))

        if exception_message == '':
            print("Lexically correct")
        else:
            print(exception_message)


main = Main()
main.run()
