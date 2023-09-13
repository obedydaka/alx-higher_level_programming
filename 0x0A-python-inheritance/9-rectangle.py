#!/usr/bin/python3|
# -*- coding: utf-8 -*-
"""
Created on Thu 14 Sep 2023 00:06

@author: Obedy Daka
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A Rectangle class shape, inheirts from BaseGeometry
    """
    def __init__(self, width, height):
        """
        init function for Rectangle

        Attributes:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        str funtion for rectangle

        Returns:
            Return width/height
        """
        return '[Rectangle] ' + str(self.__width) + '/' + str(self.__height)

    def area(self):
        """
        Calculates Area of the rectangle

        Return:
           The Area of the rectangle
        """
        return self.__width * self.__height
