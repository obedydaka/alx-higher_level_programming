#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue 12 Sep 2023 22:04

@author: Obedy Daka
"""


def write_file(filename="", text=""):
    """
    Writes input text to a utf-8 encoded file

    Arguments:
        filename (str): The name of the file to open
        text (str): The text to write in

    Return:
        A file with text written
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
