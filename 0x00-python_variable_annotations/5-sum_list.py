#!/usr/bin/env python3
"""Module documentation"""
import typing


def sum_list(input_list: typing.List[float]) -> float:
    """function sum_list which takes a list
    input_list of floats as argument and returns their sum as a float."""
    sum = 0
    for f in input_list:
        sum += f
    return sum
