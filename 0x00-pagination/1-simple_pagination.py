#!/usr/bin/env python3
"""This module is for task n.0"""


from typing import Tuple, List
import csv


def index_range(page: int, page_size: int) -> Tuple:
    """this fucntion returns the atart and the end indexes"""
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)


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
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        self.dataset()
        re_tup = index_range(page, page_size)
        if (len(self.__dataset[0]) <= re_tup[0]):
            return []
        else:
            return self.__dataset[re_tup[0]: re_tup[1]]
