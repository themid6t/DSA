import unittest
from separateChaining import HashTable

class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.hash_table = HashTable(10)
        self.hash_table.put("name", "Alice")
        self.hash_table.put("age", 30)
        self.hash_table.put("city", "Wonderland")

    def test_put_and_get(self):
        self.assertEqual(self.hash_table.get("name"), "Alice")
        self.assertEqual(self.hash_table.get("age"), 30)
        self.assertEqual(self.hash_table.get("city"), "Wonderland")

    def test_update_existing_key(self):
        self.hash_table.put("age", 31)
        self.assertEqual(self.hash_table.get("age"), 31)

    def test_remove_key(self):
        self.hash_table.remove("age")
        with self.assertRaises(KeyError):
            self.hash_table.get("age")

    def test_remove_non_existing_key(self):
        with self.assertRaises(KeyError):
            self.hash_table.remove("job")

if __name__ == '__main__':
    unittest.main()
