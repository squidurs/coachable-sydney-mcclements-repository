class Node:

    def __init__(self, key: int, value: int):
        """
        Represents a node in a doubly-linked list for the LRU Cache.

        Attributes:
            key (int): The key of the cache entry.
            value (int): The value of the cache entry.
            prev (Node): The previous node in the list.
            next (Node): The next node in the list.
        """
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    """
    Implements a Least Recently Used (LRU) Cache using a hashmap and a doubly-linked list.

    Attributes:
        capacity (int): The maximum capacity of the cache.
        cache (dict): The hashmap storing key-node pairs.
        left (Node): Dummy node for the least recently used end of the list.
        right (Node): Dummy node for the most recently used end of the list.
    """

    def __init__(self, capacity: int):
        """
        Initializes the LRUCache with a given capacity.
        """
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def _remove(self, node: Node):
        """
        Removes a node from the doubly-linked list.
        """
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def _insert(self, node: Node) -> None:
        """
        Inserts a node at the most recently used position (right end of the list).
        """
        prev = self.right.prev
        nxt = self.right
        prev.next = node
        nxt.prev = node
        node.prev = prev
        node.next = nxt


    def get(self, key: int) -> int:
        """
        Retrieves the value of a key from the cache if it exists.
        If the key is found, it is marked as the most recently used.
        """
        if not key in self.cache:
            return -1
        self._remove(self.cache[key])
        self._insert(self.cache[key])
        return self.cache[key].value


    def put(self, key: int, value: int) -> None:
        """
        Adds or updates a key-value pair in the cache. If the cache exceeds its capacity,
        the least recently used item is removed.
        """
        if key in self.cache:
            #update
            self._remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self._insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self._remove(lru)
            del self.cache[lru.key]



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

