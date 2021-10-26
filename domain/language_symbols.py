reservedWords = []
separators = []
operators = []


def readFile():
    with open('Token.in', 'r') as f:
        f.readline()
        for _ in range(12):
            separator = f.readline().strip()
            if separator == "<space>":
                separator = " "
            if separator == "<tab>":
                separator = "\t"
            if separator == "<newline>":
                separator = "\n"
            separators.append(separator)
        for _ in range(17):
            operators.append(f.readline().strip())
        for _ in range(17):
            reservedWords.append(f.readline().strip())
