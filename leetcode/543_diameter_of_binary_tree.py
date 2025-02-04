from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        """Definition for a binary tree node."""
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """Finds the diameter of a binary tree.

        The diameter is the length of the longest path between any two nodes in the tree,
        which may or may not pass through the root.

        Args:
            root (Optional[TreeNode]): The root of the binary tree.

        Returns:
            int: The diameter of the tree.
        """
        self.diameter = 0

        def dfs_height(node: TreeNode):
            if not node:
                return 0
            left_height = dfs_height(node.left)
            right_height = dfs_height(node.right)
            self.diameter = max(self.diameter, left_height + right_height)
            return 1 + max(left_height, right_height)

        dfs_height(root)
        return self.diameter
