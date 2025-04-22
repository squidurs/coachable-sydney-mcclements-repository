from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """Adds two numbers represented as linked lists and returns the result as a linked list.

        Args:
            l1 (Optional[ListNode]): The head of the first linked list representing a number (in reverse order).
            l2 (Optional[ListNode]): The head of the second linked list representing a number (in reverse order).

        Returns:
            Optional[ListNode]: A linked list representing the sum of the two numbers (in reverse order).
        """
        dummy = ListNode(0)
        tail = dummy
        carry = 0

        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            value = l1_val + l2_val + carry
            carry = value // 10
            new_node = ListNode(value % 10)

            tail.next = new_node
            tail = tail.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry:
            tail.next = ListNode(carry)

        return dummy.next
