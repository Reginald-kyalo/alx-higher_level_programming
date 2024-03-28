#!/usr/bin/python3
"""
defines a new class square a sub class of rectangle
"""
Rectangle = __import__('9-Rectangle').Rectangle


class Square(Rectangle):
    """represents a square."""

    def ___init__(self, size):
        """initializes a new square.

        Args:
            size (int): size of square
        """
        
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
