from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        Reverses a sublist of a singly linked list from position `left` to `right`.

        Args:
            head (Optional[ListNode]): Head of the linked list.
            left (int): Starting position of the sublist to reverse (1-indexed).
            right (int): Ending position of the sublist to reverse.

        Returns:
            Optional[ListNode]: Head of the modified list with the sublist reversed.
        """
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        reverse_prev = None
        cur = prev.next

        for _ in range(right - left + 1):
            next_node = cur.next
            cur.next = reverse_prev
            reverse_prev = cur
            cur = next_node

        prev.next.next = cur
        prev.next = reverse_prev

        return dummy.next
