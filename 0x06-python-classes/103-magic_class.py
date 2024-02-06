#!/usr/bin/python3
"""Definition of a MagicClass."""

import math


class MagicClass:
    """Represents a a magic Class"""

    def __init__(self, radius=0):
        """Initializer of the Magic Class.

        Arg:
            radius (float or int): The radius of the new MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius should be a number")
        self.__radius = radius

    def area(self):
        """Returns area of the Magic Class."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Returns circumference of the Magic Class."""
        return (2 * math.pi * self.__radius)
