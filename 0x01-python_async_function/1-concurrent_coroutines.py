#!/usr/bin/env python3
"""Module documentation"""
import asyncio
import typing
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """wait_n async function"""
    task = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task[i] for i in range(n)]
