#!/usr/bin/env python3
"""
Index_range to get page and page_size
"""
import csv
import math
from typing import Tuple, List


def index_range(page: int, page_size: int) -> Tuple:
    """Return a tuple of size two containing a start index and an end index"""
    return ((page - 1) * page_size, page * page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
       
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        return self.dataset()[start:end]
