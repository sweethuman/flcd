from typing import Tuple


class HashTable:
    """
    Data type of storing keys efficiently. They are stored as lists in lists. The size of the hash table decreases the
    number of possible conflicts and increases performance at the cost of increased memory.
    Position (-1,-1) means an invalid position and that the element doesn't exist.
    """

    def __init__(self, size):
        self.__items = [[] for _ in range(size)]
        self.__size = size

    def hash(self, key) -> int:
        """
        Hash of the key to find approximate position in HashTable
        """
        key_sum = sum(ord(char) - ord('0') for char in key)
        return key_sum % self.__size

    def add(self, key) -> Tuple[int, int]:
        """
        Add key to HashTable if it doesn't exist already
        :return: Position where it was added, or where it already exists
        """
        if self.contains(key):
            return self.getPosition(key)
        # replaces an empty position or adds to the list
        try:
            nonePos = self.__items[self.hash(key)].index(None)
            self.__items[self.hash(key)][nonePos] = key
        except ValueError:
            self.__items[self.hash(key)].append(key)
        return self.getPosition(key)

    def contains(self, key) -> bool:
        """
        Checks if it contains the given key
        """
        return self.getPosition(key) != (-1, -1)

    def remove(self, key) -> None:
        """
        Removes item for HashTable
        :param key:
        """
        pos = self.getPosition(key)
        if pos[0] == -1:
            return
        # does not actually remove it forces items to change position
        # when a new key is added and a position is with none it will replace it so it won't consume new memory
        self.__items[pos[0]][pos[1]] = None

    def __str__(self) -> str:
        result = "Symbol Table (kept as a Hash Table using Lists)\n"
        for i in range(self.__size):
            result = result + str(i) + "->" + str(self.__items[i]) + "\n"
        return result

    def getPosition(self, key) -> Tuple[int, int]:
        """
        Calculates the position of the given key, if key is not found, it return (-1, -1) position
        """
        list_position = self.hash(key)
        try:
            list_index = self.__items[list_position].index(key)
            return list_position, list_index
        except ValueError:
            return -1, -1

    def getKeyByPosition(self, position: Tuple[int, int]):
        """
        Gets the key at the given position
        """
        return self.__items[position[0]][position[1]]
