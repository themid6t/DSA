# Implementation of min (binary)heap data structure
from math import ceil

class minHeap:
    def __init__(self):
        self.heap = []

    def _size(self):
        """ Returns the size of the heap. """
        return len(self.heap) # O(1)
    
    def _isempty(self):
        """ Class method to check if the heap is empty. """
        return self._size() == 0 # O(1)
    
    def peek(self):
        """ Views the root of the heap. """
        return self.heap[0] # O(1)
    
    def clear(self):
        """ Delets all the element in the heap. """
        del self.heap[:] # O(1)

    def poll(self):
        """ Return the smallest element of the heap i.e the root. """
        if self._isempty(): 
            return None # O(1)
        
        root = self.heap[0] 
        if self._size() == 1:
            self.heap.clear() 
            return root
        
        self.heap[0] = self.heap.pop() # O(1)
        # O(log n) where n is the number of elements in the tree
        # At worst case it needs to reach the end of the tree i.e. the height of the tree 
        self._sink(0) 
        return root

    def insert(self, value):
        """ Insert an item into the heap. """
        if value is None:
            raise ValueError
        self.heap.append(value)
        # O(log n) : at worst case the new element needs to swim up to the
        # top of the tree i.e. the height of the tree
        self._swim(self._size() - 1)

    def delete(self, value):
        """ Delete any element from the heap. """
        index = -1
        for idx in range(self._size()):
            if self.heap[idx] == value:
                index = idx
                break
        if index == -1:
            # return "Element not found in the heap."
            return
        
        self._swap(idx, self._size() - 1)
        deleted = self.heap.pop()

        return f"Deleted {deleted} from the heap."
    
    def heapify(self, arr):
        """ Convert a list of elements into a min heap. """
        # O(n log n) : it peforms insert operation which takes O(log n) n times
        for i in range(len(arr)): # O(n)
            self.insert(arr[i]) # O(log n)
        
        return self.heap

    def printHeap(self):
        print(self.heap)

    def _sink(self, i):
        """ Class method to maintain heap property, 
            sinks the element at i down the heap untill childerns are greater."""
        left_child = (2 * i) + 1
        right_child = (2 * i) + 2
        smallest = left_child

        if right_child < self._size() and self.heap[right_child] < self.heap[left_child]:
            smallest = right_child
        
        # O(log n): in worst case the element needs to sink down the entire tree
        # which take log n time. 
        if smallest < self._size():
            self._swap(i, smallest)
            self._sink(smallest)

    def _swim(self, i):
        """ Class method to maintain heap property, 
            Move the element at i up the heap until parent is smaller"""
        parent = (i - 1) // 2

        # O(log n): in worst case the element needs to swim down the entire tree
        # which take log n time.         
        if self.heap[parent] > self.heap[i] and i > 0:
            self._swap(i, parent)
            self._swim(parent)


    def _swap(self, i, j):
        """ Class method to swap the two elements in the heap. """
        # O(1)
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]