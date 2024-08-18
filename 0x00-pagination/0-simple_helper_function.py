#!/usr/bin/env python3
"""
Write a function that will paginate data
and return the starting and end indexes
"""


def index_range(page, page_size):
    """
    Find the index range of a page
    Return a tuple containing,
    Start end index of the page
    """
    end = page_size * page
    start = end - page_size
    return (start, end)
