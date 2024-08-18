#!/usr/bin/env python3
"""This module is for task n.0"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """this fucntion returns the atart and the end indexes"""
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
