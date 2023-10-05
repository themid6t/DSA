import unittest
from minHeap import minHeap

class TestMinHeap(unittest.TestCase):
    def setUp(self):
        self.heap = minHeap()
        self.heap.insert(5)
        self.heap.insert(3)
        self.heap.insert(8)
        self.heap.insert(1)

    def test_peek(self):
        self.assertEqual(self.heap.peek(), 1)

    def test_poll(self):
        self.assertEqual(self.heap.poll(), 1)
        self.assertEqual(self.heap.poll(), 3)
        self.assertEqual(self.heap.poll(), 5)
        self.assertEqual(self.heap.poll(), 8)
        self.assertIsNone(self.heap.poll())

    def test_insert(self):
        self.heap.insert(2)
        self.assertEqual(self.heap.peek(), 1)
        self.heap.insert(0)
        self.assertEqual(self.heap.peek(), 0)

    def test_delete(self):
        self.assertEqual(self.heap.delete(3), "Deleted 3 from the heap.")
        self.assertEqual(self.heap.poll(), 1)
        self.assertIsNone(self.heap.delete(7))

    def test_is_empty(self):
        empty_heap = minHeap()
        self.assertTrue(empty_heap._isempty())
        self.assertFalse(self.heap._isempty())

if __name__ == "__main__":
    unittest.main()
