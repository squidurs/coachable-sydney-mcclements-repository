from typing import List, Optional
from collections import defaultdict, deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        """Represents a node in a binary tree.
        Args:
            val (int, optional): node value. Defaults to 0.
            left (_type_, optional): left child. Defaults to None.
            right (_type_, optional): right child. Defaults to None.
        """
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """Returns the vertical order traversal of a binary tree.

        Args:
            root (Optional[TreeNode]): The root of the binary tree.

        Returns:
            List[List[int]]: A list of lists containing the nodes' values in vertical order.
        """
        if not root:
            return []

        column_to_nodes_map = defaultdict(list)
        queue = deque([(0,root)])

        res = []

        leftmost_col = float('inf')
        rightmost_col = float('-inf')

        while queue:
            col, node = queue.popleft()

            if node is None:
                continue

            column_to_nodes_map[col].append(node.val)
            leftmost_col = min(leftmost_col, col)
            rightmost_col = max(rightmost_col, col)

            queue.append((col - 1, node.left))
            queue.append((col + 1, node.right))

        for column in range(leftmost_col, rightmost_col + 1):
            res.append(column_to_nodes_map[column])

        return res
