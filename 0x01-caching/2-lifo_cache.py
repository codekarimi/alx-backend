#!/usr/bin/env python3
"""
LIFO caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFO Caching implimentation
    """
    def __init__(self):
        """
        Initializer for the class LIFO
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first = sorted(self.cache_data.keys())[-1]
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
