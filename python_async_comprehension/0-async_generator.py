#!/usr/bin/env python3
"""defines an asynchronous generator yielding random numbers."""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Yield a random float between 0 and 10, one at a time, 10 times, """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
