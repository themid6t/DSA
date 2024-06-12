# Implementation of union find ds 

class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, p):
        if self.parent[p] != p:
            pass

    def union(self, p, q):
        pass

    def connected(self, p, q):
        """
        Checks if elements 'p' and 'q' are in the same set.
        Returns: True if 'p' and 'q' are in same set, False otherwise. 
        """
        return self.find(p) == self.find(q)

    def component_size(self, p):
        """
        Returns the size of the set to which 'p' belongs.
        """
        return self.sz[self.find(p)]