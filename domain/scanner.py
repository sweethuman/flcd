import re
from typing import List, Tuple

from domain.language_symbols import *


class Scanner:
    """
    Parses a file into it's respective tokens.
    """

    @staticmethod
    def getStringToken(line: str, index: int) -> Tuple[str, int]:
        """
        Gets the string token from the line at the given index. Index has to be placed at the quote, not after it.
        :param line: Line to process
        :param index: Current position in the line
        :return: The extracted token and the new position in the line
        """
        token = ''
        quotes = 0

        while index < len(line) and quotes < 2:
            if line[index] == '"':
                quotes += 1
            token += line[index]
            index += 1

        return token, index

    @staticmethod
    def getCharToken(line: str, index: int) -> Tuple[str, int]:
        """
        Gets the string token from the line at the given index. Index has to be placed at the quote, not after it.
        :param line: Line to process
        :param index: Current position in the line
        :return: The extracted token and the new position in the line
        """
        token = ''
        quotes = 0

        while index < len(line) and quotes < 2:
            if line[index] == "'":
                quotes += 1
            token += line[index]
            index += 1

        return token, index

    @staticmethod
    def isPartOfOperator(char) -> bool:
        """
        Checks if this specific character is part of an operator. Used to start the check for the full operator
        """
        return any(char in op for op in operators)

    def getOperatorToken(self, line: str, index: int) -> Tuple[str, int]:
        """
        Gets the operator token from the line at the given index.
        :param line: Line to process
        :param index: Current position in the line
        :return: The extracted token and the new position in the line
        """
        token = ''

        while index < len(line) and self.isPartOfOperator(line[index]):
            token += line[index]
            index += 1

        return token, index

    def tokenize(self, line: str) -> List[str]:
        """
        Takes a line and separates it into the tokens
        :param line: line to tokenize
        :return: list of tokens
        """
        token = ''
        index = 0
        tokens = []
        while index < len(line):
            regComp = re.match(r'^[\+\-][0-9](\.?[0-9]+)?', line[index:])

            if regComp is not None:
                if token:
                    tokens.append(token)
                tokens.append(regComp[0])
                index += len(regComp[0])
            elif self.isPartOfOperator(line[index]):
                if token:
                    tokens.append(token)
                token, index = self.getOperatorToken(line, index)
                tokens.append(token)
                token = ''

            elif line[index] == '"':
                if token:
                    tokens.append(token)
                token, index = self.getStringToken(line, index)
                tokens.append(token)
                token = ''

            elif line[index] == "'":
                if token:
                    tokens.append(token)
                token, index = self.getCharToken(line, index)
                tokens.append(token)
                token = ''

            elif line[index] in separators:
                if token:
                    tokens.append(token)
                token, index = line[index], index + 1
                tokens.append(token)
                token = ''

            else:
                token += line[index]
                index += 1
        if token:
            tokens.append(token)
        return tokens

    @staticmethod
    def isIdentifier(token: str) -> bool:
        """
        Check if a token is an identifier
        """
        return re.match(r'^[a-z]([a-zA-Z]|[0-9])*$', token) is not None

    @staticmethod
    def isConstant(token: str) -> bool:
        """
        Check if a token is a constant. Constant means it's either a positive or negative number, float or a string
        with the quotes
        """
        return re.match(r'^(0|([+-]?[1-9][0-9]*)|([+-]?[0-9]\.[0-9]+))$|^\".\"$|^\".*\"$|^\'[a-zA-Z0-9]\'$', token) is not None
    #
