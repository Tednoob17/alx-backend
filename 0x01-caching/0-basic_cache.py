#!/usr/bin/python3
"""Basic Caching System"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Basic Cache class that inherits from BaseCaching and is a caching system
    """

    def put(self, key, item):
        """
        Assign to the dictionnary item to the key
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Return the value linked to the key
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
