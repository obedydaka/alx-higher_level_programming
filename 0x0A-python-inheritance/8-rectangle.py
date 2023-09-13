#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thu 14 Sep 2023 00:03

@author: Obedy Daka
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A Rectangle class shape, inheirts from BaseGeometry
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
