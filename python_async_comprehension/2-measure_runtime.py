#!/usr/bin/env python3
"""measures the runtime of running async_comprehension 4 times in parallel."""

import asyncio
import time
from typing import Callable
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Run 4 times in parallel and return total elapsed time."""
    start = time.perf_counter()

    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    end = time.perf_counter()
    return end - start
