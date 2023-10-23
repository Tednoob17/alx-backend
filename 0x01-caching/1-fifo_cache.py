#!/usr/bin/python3
"""FIFOCache System"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class that inherits from BaseCaching and is FIFO caching system
    """
    def __init__(self):
        """
        Initialize
        """
        super().__init__()

    def put(self, key, item):
        """
        Assign to the dictionnary item to the key
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first = list(self.cache_data)[0]
            print("DISCARD: {}".format(first))
            self.cache_data.pop(first)
        self.cache_data[key] = item

    def get(self, key):
        """
        Return the value linked to the key
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
