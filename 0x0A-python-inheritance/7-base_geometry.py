#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 2023 23:58

@author: Obedy Daka
"""


class BaseGeometry():
    """
    An empty class
    """
    pass

    def area(self):
        """
        Public instance method that calculates Area

        Raises:
            Exception if Area is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method that validates integer input
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        elif value <= 0:
            raise ValueError(name + " must be greater than 0")
