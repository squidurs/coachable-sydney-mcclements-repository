from typing import Optional, Tuple

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
        def height_and_diameter(node: Optional[TreeNode]) -> Tuple[int, int]:
            """Helper function to compute height and diameter for the subtree rooted at 'node'

            Recursive relation:
            - If the node is None, return (0, 0).
            - Otherwise, compute the height and diameter for the left and right subtrees.
            - The height of the current node is 1 + the maximum height of its left and right subtrees.
            - The diameter at the current node is the maximum of:
                a. left_height + right_height (the longest path passing through the node),
                b. left_diameter (max diameter found in the left subtree)
                c. right_diameter (max diameter found in the right subtree)

            Args:
                node (Optional[TreeNode]): The root of the current subtree.

            Returns:
                Tuple[int, int]: height, diameter of the subtree
            """
            if not node:
                return 0, 0

            left_height, left_diameter = height_and_diameter(node.left)
            right_height, right_diameter = height_and_diameter(node.right)

            height = 1 + max(left_height, right_height)
            diameter = max(left_height + right_height, left_diameter, right_diameter)

            return height, diameter

        _, diameter = height_and_diameter(root)
        return diameter
