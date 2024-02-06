#!/usr/bin/python3
"""This defines a class Square."""


class Square:
    """To represent a square"""

    def __init__(self, size=0):
        """Initizializes a square class.

        Args:
            size (int): For the new square's size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
