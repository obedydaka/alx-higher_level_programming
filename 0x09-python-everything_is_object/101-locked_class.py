#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue September 6 02:03:45 2023

@author: Obedy Daka
"""


class LockedClass:
    """
    A locked class that only lets the user dynamically create the instance
    attribute 'first_name'
    """
    __slots__ = ['first_name']
