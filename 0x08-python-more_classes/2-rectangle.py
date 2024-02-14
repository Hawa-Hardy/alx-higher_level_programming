#!/usr/bin/python3
"""Rectangle class definition"""


class Rectangle:
    """Mimics a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle obj.

        Args:
            width (int): The new rectangle's width.
            height (int): New rectangle's height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets and set the Rectangle width."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets and sets the Rectangle height."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns area of Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns perimeter of Rectangle obj."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
