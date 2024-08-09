#!/usr/bin/env python3
"""asynchronous coroutine that takes in an integer argument (max_delay"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """with a default value of 10) named wait_random"""
    random_number = random.uniform(0, max_delay)
    await asyncio.sleep(random_number)
    return random_number
