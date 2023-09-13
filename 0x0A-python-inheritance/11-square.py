#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thu 14 Sep 2023 00:13

@author: Obedy Daka
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(BaseGeometry):
    """
    A Square class shape, inheirts from BaseGeometry
    """
    def __init__(self, size):
        """"
        Init function for Square

        Attributes:
            size (int): The size of the Square
        """
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """
        str funtion to print with/height

        Returns:
            Return width/height
        """
        return '[Square] ' + str(self.__size) + '/' + str(self.__size)

    def area(self):
        """
        A function that calculates the Area of the Square
        """
        return self.__size ** 2
