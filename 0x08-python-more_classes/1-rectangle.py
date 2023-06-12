#!/usr/bin/python3
"""
defines a class Rectangle
"""

class Rectangle:
    """empty representationof a rectangle"""
    def __init__(self, width=0, height=0):
        """initializes objects dimensions"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """getter for private instance attribute width"""
        return self.width

    @width.setter
    def width(self, value):
        """setter for the private instance attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for private instance attribute height"""
        return self.width

    @height.setter
    def height(self, value):
        """setter for the private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value


