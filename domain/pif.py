class ProgramInternalForm:
    """
    Stores all the tokens in order, with their link to the symbol table
    Position (-1,-1) means the token is a reserved word, operator or separator.
    """
    def __init__(self):
        self.__content = []

    def add(self, token, pos):
        """
        Add token to pif
        :param token: Token to add
        :param pos: Position of the token if symbol, otherwise (-1,-1)
        """
        self.__content.append((token, pos))

    def __str__(self):
        result = ""
        for pair in self.__content:
            token = pair[0] if pair[0] != '\t' else '\\tab'
            result += token + "->" + str(pair[1]) + "\n"
        return result
