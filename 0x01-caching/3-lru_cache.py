#!/usr/bin/env python3
"""
LRU caching
"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    LRU Caching implementation
    """
    def __init__(self):
        """
        Initializer for the class LRU
        """
        super().__init__()
        self.order = OrderedDict()

    def put(self, key, item):
        """
        Add an item to the cache
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded_key, _ = self.order.popitem(last=False)
            print(f"DISCARD: {discarded_key}")
            self.cache_data.pop(discarded_key)
        self.order[key] = None
        self.cache_data[key] = item

    def get(self, key):
        """
        Get an item from the cache
        """
        if key is None or key not in self.cache_data:
            return None
        value = self.cache_data[key]
        del self.order[key]
        self.order[key] = None
        return value
