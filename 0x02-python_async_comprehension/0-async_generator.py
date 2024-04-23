#!/usr/bin/env python3
"""Module documentation"""
import asyncio
import random


async def async_generator():
    """ coroutine async_generator """
    for _ in range(10):
        yield random.uniform(0, 10)
        await asyncio.gather(asyncio.sleep(1))
