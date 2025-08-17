#!/usr/bin/env python3
"""
Simple pagination utilities and a Server class to paginate
the Popular_Baby_Names.csv dataset.
"""

import csv
from typing import List, Tuple


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
