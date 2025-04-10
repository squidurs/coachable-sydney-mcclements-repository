from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Reverses a singly linked list by iterating over the list and setting each
        node's `next` pointer to the previous node.

        Args:
            head (Optional[ListNode]): The head of the original linked list.

        Returns:
            Optional[ListNode]: The new head of the reversed linked list.
        """
        cur = head
        prev = None

        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node

        return prev
