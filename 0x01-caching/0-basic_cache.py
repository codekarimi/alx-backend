#!/usr/bin/env python3
"""
BasicCache implimentation
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    BaseCache class
    """
    def __init__(self):
        """
        Initiliaze
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Get an item from the cache
        """
        if key is None:
            return
        return self.cache_data.get(key)
