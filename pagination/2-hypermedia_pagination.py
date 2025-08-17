#!/usr/bin/env python3
"""
Hypermedia pagination utilities and a Server class to paginate
the Popular_Baby_Names.csv dataset.
"""

import csv
import math
from typing import Dict, List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Compute the start and end indices for a page of a paginated list.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple of (start_index, end_index) for slicing.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """Initialize the server with an empty dataset cache."""
        self.__dataset: List[List[str]] | None = None

    def dataset(self) -> List[List[str]]:
        """
        Return the cached dataset, loading it from CSV on first access.

        Returns:
            List[List[str]]: The dataset rows (excluding the header).
        """
        if self.__dataset is None:
            with open(self.DATA_FILE, encoding="utf-8") as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        """
        Return a page of the dataset based on 1-indexed page and page_size.

        Validates that both arguments are integers greater than 0.
        Uses index_range to compute slice bounds. If the start index is
        beyond the dataset length, returns an empty list.

        Args:
            page (int): The page number (1-indexed). Defaults to 1.
            page_size (int): Number of items per page. Defaults to 10.

        Returns:
            List[List[str]]: The list of rows for the requested page.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        data = self.dataset()
        start, end = index_range(page, page_size)

        if start >= len(data):
            return []
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, object]:
        """
        Return hypermedia-style pagination metadata and data for a given page.

        The returned dictionary contains:
            - page_size: length of the returned page (may be 0 if out of range)
            - page: current page number
            - data: the actual page data (list of rows)
            - next_page: next page number or None if at/after the end
            - prev_page: previous page number or None if on the first page
            - total_pages: total number of pages as an integer

        Args:
            page (int): The page number (1-indexed). Defaults to 1.
            page_size (int): Number of items per page. Defaults to 10.

        Returns:
            Dict[str, object]: Hypermedia pagination dict.
        """
        # Use get_page (includes assertions and slicing)
        page_data = self.get_page(page, page_size)

        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size) if page_size else 0

        # Compute prev/next
        prev_page = page - 1 if page > 1 else None

        # Determine if there is a next page: only if current slice end < total_items
        start, end = index_range(page, page_size)
        next_page = page + 1 if end < total_items else None

        return {
            "page_size": len(page_data),
            "page": page,
            "data": page_data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }
