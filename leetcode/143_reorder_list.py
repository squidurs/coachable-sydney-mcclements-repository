from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """Reorders the linked list to follow the pattern: L0 -> Ln → L1 -> Ln-1 -> L2 -> ...

        Steps:
        1. Use slow and fast pointers to find the middle of the list.
        2. Reverse the second half of the list.
        3. Merge the two halves in-place.

        This modifies the list in-place without returning anything.
        """
        if not head or not head.next:
            return

        # Step 1: Find the middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse second half
        prev = None
        cur = slow
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node

        # Step 3: Merge the two halves
        first = head
        second = prev
        while second.next:
            first_nxt = first.next
            second_nxt = second.next

            first.next = second
            second.next = first_nxt
            first = first_nxt
            second = second_nxt
