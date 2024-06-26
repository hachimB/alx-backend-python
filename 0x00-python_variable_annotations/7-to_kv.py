#!/usr/bin/env python3
""" Module documentation """
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """function to_kv that takes a string k
    and an int OR float v as arguments and returns a tuple."""
    return (k, v**2)
