from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Finds the node where the cycle begins in a linked list, if a cycle exists.
        Uses Floyd's Tortoise and Hare algorithm:
        - First detects a cycle by using slow and fast pointers.
        - If a cycle is found, resets one pointer to the head and moves both
          one step at a time until they meet again. The meeting point is the
          start of the cycle.

        Args:
            head (Optional[ListNode]): Head of the linked list.

        Returns:
            Optional[ListNode]: The node where the cycle begins, or None if no cycle exists.
        """
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow

        return None
