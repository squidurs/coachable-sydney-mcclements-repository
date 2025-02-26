import unittest
from io import StringIO
import sys

class Node:
    def __init__(self, key: str, value: int):
        self.key = key
        self.value = value
        self.next = None

class HashTable:

    def __init__(self, max_size: int):
        self.max_size = max_size
        self.table = [None for _ in range(max_size)]
        self.size = 0

    def _hash(self, key: str) -> int:
        hash_code = 0
        for char in key:
            hash_code = (hash_code + ord(char)) % self.max_size
        return hash_code

    def put(self, key: str, value: int) -> None:
        idx = self._hash(key)
        new_node = Node(key, value)

        if self.table[idx]:
            cur = self.table[idx]
            while cur:
                if cur.key == key:
                    cur.value = value
                    return
                if not cur.next:
                    break
                cur = cur.next

        if self.size >= self.max_size:
            print("Error. Table full.")
            return
        if not self.table[idx]:
            self.table[idx] = new_node
        else:
            cur.next = new_node
            
        self.size += 1


    def get(self, key) -> int:
        idx = self._hash(key)
        cur = self.table[idx]

        while cur:
            if cur.key == key:
                return cur.value
            cur = cur.next
        print("Key not found")


class TestHashTable(unittest.TestCase):
    def test_create(self):
        hash_table = HashTable(53)

        self.assertEqual(hash_table.size, 0)
        self.assertEqual(len(hash_table.table), 53)

    def test_put(self):
        hash_table = HashTable(7)
        hash_table.put("a", 1)

        self.assertEqual(hash_table.table[6].key, "a")
        self.assertEqual(hash_table.table[6].value, 1)

    def test_put_collision(self):
        hash_table = HashTable(7)
        hash_table.put("ab", 1)
        hash_table.put("ba", 2)

        self.assertEqual(hash_table.table[6].key, "ab")
        self.assertEqual(hash_table.table[6].value, 1)
        self.assertEqual(hash_table.table[6].next.key, "ba")
        self.assertEqual(hash_table.table[6].next.value, 2)

    def test_change_value(self):
        hash_table = HashTable(7)
        hash_table.put("a", 1)
        hash_table.put("a", 2)

        self.assertEqual(hash_table.table[6].value, 2)

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
