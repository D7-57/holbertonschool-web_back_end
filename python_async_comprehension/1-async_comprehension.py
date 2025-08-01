#!/usr/bin/env python3
"""collects values from an async generator using comprehension."""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collect 10 random numbers from async_generator using async."""
    return [value async for value in async_generator()]
