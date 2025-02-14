from typing import Optional, List
from collections import deque

# TEST CASES

# 1. Skewed tree with mixed left and right nodes
#       1
#      / \
#     2   3
#    /
#   4
#  / \
# 5   6
# Expected output: [1, 3, 4, 6]

# 2. Perfect binary tree
#         1
#        / \
#       2   3
#      / \  /\
#     4  5  6 7
# Expected output: [1, 3, 7]

# 3. Left-skewed tree
#      1
#     /
#    2
#   /
#  3
# /
# 4
# Expected output: [1, 2, 3, 4]

# 4. Right-skewed tree
# 1
#  \
#   2
#    \
#     3
#      \
#       4
# Expected output: [1, 2, 3, 4]

# 5. Single node tree
# 1
# Expected output: [1]


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        """Definition for a binary tree node."""
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Returns the right-side view of a binary tree by capturing the rightmost node at each level.

        Args:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            List[int]: A list of values representing the rightmost nodes at each level of the tree
        """

        if not root:
            return []

        queue = deque([root])
        rightmost_nodes = []

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                if i == level_size - 1:
                    rightmost_nodes.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return rightmost_nodes
