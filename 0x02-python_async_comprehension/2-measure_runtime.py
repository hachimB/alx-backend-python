#!/usr/bin/env python3
import asyncio
import typing
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure_runtime"""
    start_time = time.time()

    # Create a list of four futures
    tasks: typing.List[asyncio.Future] = [async_comprehension()
                                          for _ in range(4)]

    # Use asyncio.gather to run them concurrently
    await asyncio.gather(*tasks)

    end_time = time.time()

    return end_time - start_time
