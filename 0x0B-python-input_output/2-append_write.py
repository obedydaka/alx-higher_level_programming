#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue 12 Sep 2023 22:07

@author: Obedy Daka
"""


def append_write(filename="", text=""):
    """
    Appends input text into a utf-8 encoded text file

    Arguments:
        filename (str): The name of the file to open
        text (str): The text to append

    Return:
        A file with appened text
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
