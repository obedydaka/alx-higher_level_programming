#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue 12 Sep 2023 22:01

@author: Obedy Daka
"""

def read_file(filename=""):
    """
    Reads the file

    Arguments:
        filename (str): The name of the file to open
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
