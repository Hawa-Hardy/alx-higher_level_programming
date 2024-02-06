#!/usr/bin/python3
"""This defines a class Square."""

class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initizializes a square class.

        Args:
            size (int): For the new square's size
        """
        self.size = size

    @property
    def size(self):
        """Gets and sets a size for the square."""
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

    def __eq__(self, other):
        """Defines == comparator to a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Defines != comparator to a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Defines < comparator to a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Defines <= comparator to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Defines > comparator to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Defines >= comparator to a Square."""
        return self.area() >= other.area()
