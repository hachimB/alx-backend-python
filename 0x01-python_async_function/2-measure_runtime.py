#!/usr/bin/env python3
"""Module documentation"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time_sync(n: int, max_delay: int) -> float:
    """measure_time function with integers n and max_delay as arguments
    that measures the total execution time for wait_n(n, max_delay),
    and returns total_time / n"""
    start_time = time.perf_counter()
    await wait_n(n, max_delay)
    total_time = time.perf_counter() - start_time
    return (total_time / n)


def measure_time(n: int, max_delay: int) -> float:
    """Synchronous wrapper for measure_time"""
    return asyncio.run(measure_time_sync(n, max_delay))
