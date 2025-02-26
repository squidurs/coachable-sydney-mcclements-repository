import unittest
from io import StringIO
import sys

class HashTable:

    def __init__(self, max_size: int):
        self.max_size = max_size
        self.table = [[] for _ in range(max_size)]
        self.size = 0

    def _hash(self, key: str) -> int:
        hash_code = 0
        for char in key:
            hash_code = (hash_code + ord(char)) % self.max_size
        return hash_code

    def put(self, key: str, value: int) -> None:
        idx = self._hash(key)
        for i, (table_key, _) in enumerate(self.table[idx]):
            if table_key == key:
                self.table[idx][i] = (key, value)
                return
        if self.size == self.max_size:
            print("Error. Table full.")
        else:
            self.table[idx].append((key, value))
            self.size += 1

    def get(self, key) -> int:
        idx = self._hash(key)
        for table_key, value in self.table[idx]:
            if table_key == key:
                return value
        print("Key not found")

class TestHashTable(unittest.TestCase):
    def test_create(self):
        hash_table = HashTable(53)

        self.assertEqual(hash_table.size, 0)
        self.assertEqual(len(hash_table.table), 53)

    def test_put(self):
        hash_table = HashTable(7)
        hash_table.put("a", 1)

        self.assertEqual(hash_table.table[6][0], ("a", 1))

    def test_put_collision(self):
        hash_table = HashTable(7)
        hash_table.put("ab", 1)
        hash_table.put("ba", 2)

        self.assertEqual(hash_table.table[6][0], ("ab", 1))
        self.assertEqual(hash_table.table[6][1], ("ba", 2))

    def test_change_value(self):
        hash_table = HashTable(7)
        hash_table.put("a", 1)
        hash_table.put("a", 2)

        self.assertEqual(hash_table.table[6][0], ("a", 2))

    def test_put_at_capacity(self):
        hash_table = HashTable(1)
        hash_table.put("a", 1)
        captured_output = StringIO()
        sys.stdout = captured_output
        hash_table.put("b", 2)
        sys.stdout = sys.__stdout__

        self.assertIn("Error. Table full.", captured_output.getvalue())

    def test_get(self):
        hash_table = HashTable(7)
        hash_table.put("a", 1)

        self.assertEqual(1, hash_table.get("a"))

    def test_get_invalid_key(self):
        hash_table = HashTable(7)
        captured_output = StringIO()
        sys.stdout = captured_output
        hash_table.get("b")
        sys.stdout = sys.__stdout__

        self.assertIn("Key not found", captured_output.getvalue())
