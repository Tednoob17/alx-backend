#!/usr/bin/python3
"""LRUCache System"""
from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """
    LFUCache class that inherits from BaseCaching and is LFU caching system
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
        if key not in self.cache_data:
            if len(self.cache_data) >= self.MAX_ITEMS:
                last, _ = self.cache_data.popitem()
                print("DISCARD: {}".format(last))
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Return the value linked to the key
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
