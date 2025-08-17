#!/usr/bin/env python3
"""
Simple pagination module
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start and end indexes.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the server with no cached dataset."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset

        Returns:
            List[List]: The dataset without the header row.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return the appropriate page of the dataset based on pagination.

        Args:
            page (int, optional): The page number (1-indexed).
            page_size (int, optional): The number of items per page.

        Returns:
            List[List]: The requested page of the dataset.
        """
        assert isinstance(
            page, int) and page > 0
        assert isinstance(
            page_size, int) and page_size > 0

        dataset = self.dataset()
        start_idx, end_idx = index_range(page, page_size)

        if start_idx >= len(dataset):
            return []

        return dataset[start_idx:end_idx]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Return a dictionary containing pagination information

        Args:
            page (int, optional): The page number (1-indexed).
            page_size (int, optional): The number of items per page.

        Returns:
            dict: A dictionary containing:
                - page_size (int): Number of items on the current page.
                - page (int): Current page number.
                - data (List[List]): The dataset page.
                - next_page (int or None): Next page number, or None.
                - prev_page (int or None): Previous page number, or None
                - total_pages (int): Total number of pages in the dataset.
        """
        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        hypermedia = {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages,
        }

        return hypermedia
