from __future__ import annotations
from collections import defaultdict
import heapq

class Node:
    def __init__(self, value: int | None = None):
        """
        Represents a node in a doubly-linked list for the Max Stack.

        Attributes:
            value (int | None): The integer value stored in the node (or None for dummy nodes).
            prev (Node | None): Pointer to the previous node in the list.
            next (Node | None): Pointer to the next node in the list.
        """
        self.value = value
        self.prev = None
        self.next = None


class MaxStack:
    """
    A stack that supports push, pop, top, retrieving the maximum element,
    and removing the maximum element using a combination
    of a doubly linked list, a max-heap, and a hash map.
    """

    def __init__(self):
        """
        Initializes an empty MaxStack.

        Attributes:
            value_to_nodes_map (defaultdict[list]): A mapping of values to
                their corresponding nodes in the doubly linked list, allowing
                efficient retrieval and removal of the most recent instance
                of a value.
            max_heap (list): A max-heap implemented as a min-heap of negative values
                to support efficient retrieval of the maximum element.
            left (Node): Dummy node representing the start of the doubly linked list.
            right (Node): Dummy node representing the end of the doubly linked list.
        """
        self.value_to_nodes_map = defaultdict(list)
        self.max_heap = []
        self.left = Node(None)
        self.right = Node(None)
        self.left.next = self.right
        self.right.prev = self.left



    def push(self, x: int) -> None:
        """
        Pushes an element onto the stack.

        Args:
            x (int): The value to push onto the stack.

        This method inserts the element into the doubly linked list,
        updates the hash map for fast lookup, and maintains the max-heap.
        """
        new_node = Node(x)
        self.value_to_nodes_map[x].append(new_node)
        heapq.heappush(self.max_heap, -x)

        self.right.prev.next = new_node
        new_node.prev = self.right.prev
        new_node.next = self.right
        self.right.prev = new_node


    def pop(self) -> int:
        """
        Removes and returns the top element of the stack.

        Returns:
            int: The value of the removed top element.

        This method removes the last inserted element from both the
        doubly linked list and the hash map.
        """
        node_to_remove = self.right.prev
        val = node_to_remove.value

        if len(self.value_to_nodes_map[val]) > 1:
            self.value_to_nodes_map[val].pop()
        else:
            del self.value_to_nodes_map[val]

        self._remove(node_to_remove)
        return val


    def top(self) -> int:
        """
        Retrieves the top element without removing it.

        Returns:
            int: The value of the top element.
        """
        return self.right.prev.value


    def peekMax(self) -> int:
        """
        Retrieves the maximum element currently in the stack without removing it.

        Returns:
            int: The maximum value in the stack.

        The method ensures the heap is cleaned of stale values (values no longer
        present in the linked list and hash map) before returning the true maximum.
        """
        while -self.max_heap[0] not in self.value_to_nodes_map:
            heapq.heappop(self.max_heap)
        return -self.max_heap[0]


    def popMax(self) -> int:
        """
        Removes and returns the maximum element in the stack.

        Returns:
            int: The maximum value removed from the stack.

        If multiple instances of the maximum element exist, only the most
        recently added instance is removed. The method ensures heap integrity
        by relying on `peekMax()` to clean up stale values before retrieval.
        """
        max_val = self.peekMax()
        max_node = self.value_to_nodes_map[max_val].pop()

        if not self.value_to_nodes_map[max_val]:
            del self.value_to_nodes_map[max_val]

        self._remove(max_node)
        return max_val

    def _remove(self, node: Node):
        """Removes a given node from the doubly linked list.

        Args:
            node (Node): The node to remove.
        """
        node.prev.next = node.next
        node.next.prev = node.prev
        