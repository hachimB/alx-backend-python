#!/usr/bin/env python3
"""Module documentation"""
import asyncio
import random


async def wait_random(max_delay: int = 10):
    """asynchronous coroutine wait_random"""
    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand
