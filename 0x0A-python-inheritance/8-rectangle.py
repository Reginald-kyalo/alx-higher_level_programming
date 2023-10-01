#!/usr/bin/python3
"""defines class rectangle that inherits from basegeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """represents rectangle class from basegeometry"""

    def __init__(self, width, height):
        """initializes new rectangle.

        Args:
            width (int): width of new rectengle
            height (int): height of new rectangle
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

