# Implementation of a hash table using modulo hash function and separate chaining

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
    
    def _hash_function(self, key):
        # hash function to convert a key into the index of the table
        return hash(key) % self.size 

    def put(self, key, value):
        # Insert a key value pair into the hash table
        index = self._hash_function(key) 
        if self.table[index] is None:
            # Creates a new chain if index was empty
            self.table[index] = [[key, value]]
        else:
            for pair in self.table[index]:
                # if the key already exists update the value 
                if pair[0] == key:
                    pair[1] = value
                    return
                # Or just append the pair into the chain
                self.table[index].append([key, value])

    def get(self, key):
        # retrieve the value of a key if it exists in the table
        index = self._hash_function(key)
        if self.table[index] is not None:
            for pair in self.table[index]:  # search throught the chain
                if pair[0] == key:
                    return pair[1]
        raise KeyError
    
    def remove(self, key):
        # delete a key value pair from the HashTable
        index = self._hash_function(key)
        if self.table[index] is not None:
            for i, pair in enumerate(self.table[index]):
                if pair[0] == index:
                    del self.table[index][i]
                    return
        raise KeyError