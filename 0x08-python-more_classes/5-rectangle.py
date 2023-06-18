#!/usr/bin/python3
"""
defines a class Rectangle
"""


class Rectangle:
    """empty representationof a rectangle"""
    def __init__(self, width=0, height=0):
        """initializes objects dimensions"""
        self.width = width
        self.height = height

    def __del__(self):
        """prints a string when an object is deleted"""
        print("Bye rectangle...")

    @property
    def width(self):
        """getter for private instance attribute width"""
        return self.__width

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
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        string = ""
        string += "\n".join("#" * self.__width
                            for j in range(self.__height))
        return string

    def __repr__(self):
        """return string represantion of rectangle"""
        return f"rectangle({self.__width}, {self.__height})"
