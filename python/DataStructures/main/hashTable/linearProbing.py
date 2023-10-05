# Implementation of hash table using separate chaining

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash_function(self, key):
        return hash(key) % self.size
    
    def put(self, key, value):
        pass
    
    def get(self, key):
        pass

    def remove(self, key):
        pass