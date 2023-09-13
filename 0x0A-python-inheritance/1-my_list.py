#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed 13 Sep 2023 23:39

@author: Obedy Daka
"""


class MyList(list):
    """
     class MyList that inherits from list
    """
    def print_sorted(self):
        """
        Public instance method that prints sorted list
        """
        list_copy = self[:]
        list_copy.sort()
        print(list_copy)
