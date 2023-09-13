#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed 13 Sep 2023 23:48

@author: Obedy Daka
"""


def inherits_from(obj, a_class):
    """
    Checks if object is an instance of class, or an instance of a class that\
            inherited from another
    """
    if not isinstance(a_class, type):
        raise TypeError("a_class type must be type")

    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
