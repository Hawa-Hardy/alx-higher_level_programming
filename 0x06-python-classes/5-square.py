#!/usr/bin/python3
"""This defines a class Square."""


class Square:
    """To represent a square"""

    def __init__(self, size):
        """Initizializes a square class.

        Args:
            size (int): For the new square's size
        """
        self.size = size

    @property
    def size(self):
        """Gets and sets the square's size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints the square with a #"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
