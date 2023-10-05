import unittest
from main.linkedList.linkedList import Llist

class TestLlist(unittest.TestCase):

    def setUp(self):
        self.llist = Llist()

    def test_empty_list(self):
        self.assertEqual(self.llist.size(), 0)
        self.assertTrue(self.llist.empty())
        self.assertIsNone(self.llist.front())
        self.assertIsNone(self.llist.back())

    def test_push_back(self):
        self.llist.push_back(1)
        self.assertEqual(self.llist.size(), 1)
        self.assertFalse(self.llist.empty())
        self.assertEqual(self.llist.front(), 1)
        self.assertEqual(self.llist.back(), 1)

        self.llist.push_back(2)
        self.assertEqual(self.llist.size(), 2)
        self.assertEqual(self.llist.front(), 1)
        self.assertEqual(self.llist.back(), 2)

    def test_push_front(self):
        self.llist.push_front(1)
        self.assertEqual(self.llist.size(), 1)
        self.assertFalse(self.llist.empty())
        self.assertEqual(self.llist.front(), 1)
        self.assertEqual(self.llist.back(), 1)

        self.llist.push_front(2)
        self.assertEqual(self.llist.size(), 2)
        self.assertEqual(self.llist.front(), 2)
        self.assertEqual(self.llist.back(), 1)

    def test_pop_back(self):
        self.llist.push_back(1)
        self.llist.push_back(2)
        self.llist.pop_back()
        self.assertEqual(self.llist.size(), 1)
        self.assertEqual(self.llist.front(), 1)
        self.assertEqual(self.llist.back(), 1)

        self.llist.pop_back()
        self.assertEqual(self.llist.size(), 0)
        self.assertTrue(self.llist.empty())

    def test_pop_front(self):
        self.llist.push_back(1)
        self.llist.push_back(2)
        self.llist.pop_front()
        self.assertEqual(self.llist.size(), 1)
        self.assertEqual(self.llist.front(), 2)
        self.assertEqual(self.llist.back(), 2)

        self.llist.pop_front()
        self.assertEqual(self.llist.size(), 0)
        self.assertTrue(self.llist.empty())

    def test_at_index(self):
        self.llist.push_back(1)
        self.llist.push_back(2)
        self.assertEqual(self.llist.atIndex(0), 1)
        self.assertEqual(self.llist.atIndex(1), 2)

    def test_iterator(self):
        self.llist.push_back(1)
        self.llist.push_back(2)
        self.llist.push_back(3)
        self.assertEqual(self.llist.iterator(end_pos=2, printing=False).data, 2)
        self.assertEqual(self.llist.iterator(end_pos=3, printing=False).data, 3)

if __name__ == '__main__':
    unittest.main()
