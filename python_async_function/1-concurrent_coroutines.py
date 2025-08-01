#!/usr/bin/env python3
"""runs multiple coroutines concurrently and returns sorted delays."""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times and return the list of delays"""
    delays: List[float] = []
    tasks: List[asyncio.Task] = []

    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)

    return delays
