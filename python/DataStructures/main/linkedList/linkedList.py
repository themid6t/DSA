#vector implementation of linked list

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Llist:
    def __init__(self) -> None:
        self.head = None

    def size(self) -> int:
        """ returns the size of the list """
        count = 0
        cur = self.head
        while cur:
            count += 1
            cur = cur.next
        return count
    
    def clear(self) -> None:
        """ remove all data from the list """
        cur = self.head
        while cur:
            nextNode = cur.next
            del cur
            cur = nextNode
        self.head = None
    
    def empty(self) -> bool:
        """ check if the list is empty """
        if self.head:
            return False
        return True
    
    def back(self) -> Node:
        """ return the end Node """
        if not self.empty():
            end = self.head
            while end.next:
                end = end.next
            return end.data
    
    def front(self) -> Node:
        """ return the front element """
        if not self.empty():
            return self.head.data
    
    def push_back(self, data) -> None:
        """ add data to the end of the list """
        if self.empty():
            self.head = Node(data)
            return
        end = self.back()
        end.next = Node(data)

    def push_front(self, data) -> None:
        """ add data to the front of the list """
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def pop_back(self) -> None:
        """ remove data from the end of the list """
        prev = None
        cur = self.head
        while cur.next:
            prev = cur
            cur = cur.next
        prev.next = None
        del cur
    
    def pop_front(self) -> None:
        """ remove the front element from the list """
        if self.head:
            head = self.head
            self.head = head.next
            del head

    def atIndex(self, index):
        """ return data at index """
        count = 0
        node = self.head
        while not self.empty() and count < self.size():
            if count == index:
                return node.data
            node = node.next
            count += 1
    
    def iterator(self, end_pos=None, printing=True):
        """ method to itterate through the list and return Node or prints data based on condition"""
        if not end_pos:
            end_pos = self.size() 
        if not self.empty():
            count = 0
            cur = self.head
            while count<end_pos:
                if printing:
                    print(cur.data)
                cur = cur.next
                count += 1
            if not printing:
                return cur
