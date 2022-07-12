#!/usr/bin/env python3
"""Defines a caching system adhering to the LIFO
cache replacement policy
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """A basic caching system blueprint adhering to the LIFO
    cache replacement policy
    """
    def __init__(self):
        """Initializes the caching system with features inherited
        from BaseCaching
        """
        super().__init__()

    def put(self, key, item):
        """Adds items to the cache
        If the number of items in the cache_data is
        higher than the MAX_ITEMS, the last item is discarded
        Discard with the key discarded is printed

        Args:
            key: The key to add to the cache with a value as a dict
            item: Value to be paired with the key
        """
        if key is None or item is None:
            return
        self.cache_data.update(dict({key: item}))
        cache_size = len(self.cache_data.items())
        keys = list(self.cache_data.keys())
        if cache_size > BaseCaching.MAX_ITEMS:
            d = self.cache_data.pop(keys[-2])
            print("DISCARD:", keys[-2])

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
