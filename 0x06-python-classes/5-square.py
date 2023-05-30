#!/usr/bin/python3
""" defines a square """


class Square:
    """ square with private instance attribute size """

    def __init__(self, size=0):
        """
        initializes square
        Args:
            size: size of side of square
        """

        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.size = size
        else:
            raise TypeError('size must be an integer')
    @property
    def size(self):
        """
        getter of value of size of square
        Returns:
            size of square
        """
        return self.__size
    @size.setter
    def size(self, value):
        """
        setter of value of __size
        Args:
            value(int): to be set as size
        Returns:
            None
        """
        if type(value) is int:
            if value < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = value
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """
        finds area of square
        Returns:
            the area of the square
        """

        return self.__size ** 2
    def my_print(self):
        """
        prints square using '#'
        Returns:
            None
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("".join(["#" for j in range(self.__size)]))
