#!/usr/bin/env python3
"""Defines a caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """A basic caching system blueprint
    """
    def __init__(self):
        """Initializes the caching system with features inherited
        from BaseCaching
        """
        super().__init__()

    def put(self, key, item):
        """Adds items to the cache

        Args:
            key: The key to add to the cache with a value as a dict
            item: Value to be paired with the key
        """
        if key is None or item is None:
            return
        self.cache_data.update(dict({key: item}))

    def get(self, key):
        """Gets the value of key in the cache object

        Args:
            key: The key to get the value of

        Returns:
            Value in the cache linked to key
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
