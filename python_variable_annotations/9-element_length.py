#!/usr/bin/env python3
""" function to return elements with their lengths."""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples containing the element and its length."""
    return [(i, len(i)) for i in lst]
