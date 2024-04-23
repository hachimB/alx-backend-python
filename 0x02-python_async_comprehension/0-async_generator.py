#!/usr/bin/env python3
"""Module documentation"""
import asyncio
import random
import typing


async def async_generator() -> typing.AsyncGenerator[float, None]:
    """ coroutine async_generator """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
