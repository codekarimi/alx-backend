#!/usr/bin/env python3
"""
FIFO caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFO Caching implimentation
    """
    def __init__(self):
        """
        Initializer for the class FIFO
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first = sorted(self.cache_data.keys())[0]
            print(f"DISCARD: {first}")
            self.cache_data.pop(first)
        self.cache_data[key] = item

    def get(self, key):
        """
        Get an item from the cache
        """
        if key is None:
            return
        return self.cache_data.get(key)
