#!/usr/bin/env python3
"""Defines a Class that handles data with the Last Recently used approach
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """Handles cache data with the LRU approach
    """
    def __init__(self):
        """Initializes the class and calls the parent class
        """
        super().__init__()
        self.track = {}

    def put(self, key, item):
        """Assigns to the dictionary self.cache_data the item
        value for the key 'key'
        If the number of items in self.cache_data exceeds that of
        BaseCaching.MAX_ITEMS, the least recently used item is discarded
        and the following is printed out

        ::
            DISCARD: discarded-key
        ::

        Where discarded-key is the key of the discarded item

        Args:
            key: The key of the item
            item: The value to be assigned to key
        """
        if key is None or item is None:
            return
        self.cache_data.update(dict({key: item}))
        self.track[key] = 0
        cache_size = len(self.cache_data.items())
        if cache_size > BaseCaching.MAX_ITEMS:
            sort_track = sorted(self.track.items(), key=lambda item: item[1])
            track_keys = dict(sort_track).keys()
            d = self.cache_data.pop(list(track_keys)[0])
            d = self.track.pop(list(track_keys)[0])
            print("DISCARD:", sort_track[0][0])

    def get(self, key):
        """Returns the value in self.cache_data linked to key

        Args:
            key: The key to return the value of

        Returns:
            The value in self.cache_data linked to key
        """
        if key is None or key not in self.cache_data.keys():
            return None
        self.track[key] += 1
        return self.cache_data.get(key)
