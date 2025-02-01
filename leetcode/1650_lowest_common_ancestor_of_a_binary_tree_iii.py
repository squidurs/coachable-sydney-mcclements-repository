from __future__ import annotations

class Node:
    def __init__(self, val: int, left: Node = None, right: Node = None, parent: Node = None):
        """Represents a node in a binary tree.

        Args:
            val (int): The value of the node.
            left (Node, optional): The left child of the node. Defaults to None.
            right (Node, optional): The right child of the node. Defaults to None.
            parent (Node, optional): The parent of the node. Defaults to None.
        """
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

class Solution:
    def lowestCommonAncestor(self, p: Node, q: Node) -> Node:
        """
        Finds the lowest common ancestor of two nodes using a set to track ancestors.

        Args:
            p (Node): The first node.
            q (Node): The second node.

        Returns:
            Node: The lowest common ancestor of nodes p and q.
        """
        seen = set()

        while p:
            seen.add(p)
            p = p.parent

        while q:
            if q in seen:
                return q
            q = q.parent

    def lowestCommonAncestor2(self, p: 'Node', q: 'Node') -> 'Node':
        """Finds the lowest common ancestor of two nodes using a two-pointer approach.

        Args:
            p (Node): The first node.
            q (Node): The second node.

        Returns:
            Node: The lowest common ancestor of nodes p and q.
            """
        p_copy = p
        q_copy = q

        while p_copy != q_copy:
            q_copy = q_copy.parent if q_copy else p
            p_copy = p_copy.parent if p_copy else q

        return p_copy
    