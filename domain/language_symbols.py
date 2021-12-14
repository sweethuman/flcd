reservedWords = []
separators = []
operators = []
symbols = []


def readFile():
    with open('Token.in', 'r') as f:
        f.readline()
        for _ in range(11):
            separator = f.readline().strip()
            if separator == "<space>":
                separator = " "
            if separator == "<tab>":
                separator = "\t"
            if separator == "<newline>":
                separator = "\n"
            separators.append(separator)
            symbols.append(separator)
        for _ in range(13):
            elem = f.readline().strip()
            operators.append(elem)
            symbols.append(elem)
        for _ in range(15):
            elem = f.readline().strip()
            reservedWords.append(elem)
            symbols.append(elem)
