#!/usr/bin/python3
# 4-square.py


class Square:
    """defines a square"""
    def __init__(self, size=0):
        """ïntialize the square"""
        self.size = size

        def size(self):
            """to retrieve size of the square"""
            return (self.__size)

        def size(self, value):
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

            def area(self):
                """"returns the current square area"""
                return (self.__size * self.__size)
