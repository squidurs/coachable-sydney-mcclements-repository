from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        """Definition for a Node.
        Args:
            x (int): The value of the node.
            next (Node, optional): Reference to the next node in the list.
            random (Node, optional): Reference to a random node in the list.
        """
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        Creates a deep copy of a linked list where each node has an additional random pointer.

        Args:
            head (Optional[Node]): The head of the original linked list.

        Returns:
            Optional[Node]: The head of the copied linked list.
        """
        if not head:
            return None

        original_to_copy_node_map = {}

        # First pass: create copy nodes and map them to original nodes
        cur = head
        while cur:
            copy_node = Node(cur.val)
            original_to_copy_node_map[cur] = copy_node
            cur = cur.next

        # Second pass: assign next and random pointers for each copied node
        cur = head
        while cur:
            copy_node = original_to_copy_node_map[cur]
            copy_node.next = original_to_copy_node_map[cur.next] if cur.next else None
            copy_node.random = original_to_copy_node_map[cur.random] if cur.random else None
            cur = cur.next

        return original_to_copy_node_map[head]
