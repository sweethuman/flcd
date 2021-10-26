from domain.hash_table import HashTable


class SymbolTable:
    """
    Stores the symbols and constants in the programs
    """
    def __init__(self, size) -> None:
        self.__ht = HashTable(size)

    def __str__(self) -> str:
        return str(self.__ht)

    def add(self, key):
        """
        Add symbol
        """
        return self.__ht.add(key)

    def contains(self, key):
        """
        Check if contains symbol
        """
        return self.__ht.contains(key)

    def remove(self, key):
        """
        Remove symbol
        """
        self.__ht.remove(key)

    def getPosition(self, key):
        """
        Get position of symbol
        """
        return self.__ht.getPosition(key)
