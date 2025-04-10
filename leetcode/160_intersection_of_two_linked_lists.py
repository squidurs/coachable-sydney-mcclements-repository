from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """Finds the node at which two linked lists intersect.

        Args:
            headA (Optional[ListNode]): Head of the first linked list.
            headB (Optional[ListNode]): Head of the second linked list.

        Returns:
            Optional[ListNode]: The node where the two lists intersect or None if there is no intersection.
        """
        a = headA
        b = headB

        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA

        return a
