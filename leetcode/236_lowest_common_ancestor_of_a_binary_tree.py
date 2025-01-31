class TreeNode:
    def __init__(self, x):
        """Definition for a binary tree node."""
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """Finds the lowest common ancestor (LCA) of two given nodes in a binary tree.

        Args:
            root (TreeNode): The root of the binary tree.
            p (TreeNode): First node.
            q (TreeNode): Second node.

        Returns:
            TreeNode: The lowest common ancestor of p and q.
        """
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left or right
