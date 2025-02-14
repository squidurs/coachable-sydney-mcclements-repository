from typing import Optional

# **TEST CASES**

# 1. Balanced tree
#     1
#    / \
#   2   3
# Expected output: 12 + 13 = 25

# 2. Tree with different path lengths
#     4
#    / \
#   9   0
#  / \
# 5   1
# Expected output: 495 + 491 + 40 = 1026

# 3. Left-skewed tree
#     1
#    /
#   2
#  /
# 3
# Expected output: 123

# 4. Right-skewed tree
# 1
#  \
#   2
#    \
#     3
# Expected output: 123

# 5. Single node tree
# 1
# Expected output: 1


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        """Definition for a binary tree node."""
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """
        Computes the sum of all numbers formed from root-to-leaf paths.

        Args:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            int: The total sum of all root-to-leaf numbers.
        """
        def dfs(node: TreeNode, cur_num: int) -> int:
            """
            Performs depth-first search to compute the sum of root-to-leaf numbers.

            Args:
                node (Optional[TreeNode]): The current node in traversal.
                cur_num (int): The number formed from the root to the current node.

            Returns:
                int: The sum of all numbers from root to leaf nodes.
            """
            if not node:
                return 0

            cur_num = cur_num * 10 + node.val

            if not node.left and not node.right:
                return cur_num

            return dfs(node.left, cur_num) + dfs(node.right, cur_num)

        return dfs(root, 0)
