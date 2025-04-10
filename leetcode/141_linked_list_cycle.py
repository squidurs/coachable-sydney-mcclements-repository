from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """Detects if a linked list has a cycle using Floyd's Tortoise and Hare algorithm.

        Args:
            head (Optional[ListNode]): Head of the linked list.

        Returns:
            bool: True if a cycle exists, otherwise False.
        """
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False
