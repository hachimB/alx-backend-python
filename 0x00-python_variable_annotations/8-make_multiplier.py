#!/usr/bin/env python3
"""Module documentation"""
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """function make_multiplier that takes a float
    multiplier as argument and returns a function that multiplies
    a float by multiplier."""
    def multiply(num: float) -> float:
        """function multiply that multiplies a float by multiplier."""
        return num * multiplier
    return multiply
