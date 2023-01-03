#!/usr/bin/python3


'''
module rectangle class
'''


class Rectangle():
    '''
    this is class with width and height attributes

    Attributes:
        number _of_instances (int): instances count
        print_symbol (any): print symbol
    '''

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        '''
        initiaalises class_
        '''
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        '''
        get  width
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        set width
        '''
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''
        get height
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        set height
        '''
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''
        returns rectangle area
        '''
        return self.__width * self.__height

    def perimeter(self):
        '''
        return rectangle perimeter
        '''
        if self.__height == 0 or self.__width == 0:
            return 0
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        '''
        return string repmof rectangle class
        '''
        if self.__height == 0 or self.__width == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        '''
        return string representation of rectangle classs
        '''
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        '''
        print message for every delation of a class
        '''
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
