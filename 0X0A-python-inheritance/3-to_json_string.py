#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue 12 Sep 2023 22:59

@author: Obedy Daka
"""
import json


def to_json_string(my_obj):
    """
    Returs a json string containing object's representation

    Arguments:
        my_obj (str): The inputed object to convert in json format

    Return:
        A json format text
    """
    return json.dumps(my_obj)
