#!/usr/bin/python3
"""LIFOCache System"""
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """
    LIFOCache class that inherits from BaseCaching and is LIFO caching system
    """
    def __init__(self):
        """
        Initialize
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Assign to the dictionnary item to the key
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= self.MAX_ITEMS and \
           key not in self.cache_data.keys():
            last = list(self.cache_data.keys())[-1]
            print("DISCARD: {}".format(last))
            self.cache_data.pop(last)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """
        Return the value linked to the key
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
