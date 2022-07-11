#!/usr/bin/env python3

"""Defines a pagination helper function
"""


def index_range(page: int, page_size: int) -> tuple:
    """Returns a tuple of size two containing a start
    index and an end index corresponding to the range
    of indexes to return in a list for pagination parameters

    Args:
        page: 1-indexed page numbers
        page_size: The size of the page

    Returns:
        A tuple of size two with start and end indexes
    """
    if page == 0:
        return
    if page == 1:
        return (page - 1, (page - 1) + page_size)

    return (page * 10, (page * 10) + page_size)
