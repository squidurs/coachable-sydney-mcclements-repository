from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional['ListNode'], n: int) -> Optional[ListNode]:
        """Removes the n-th node from the end of a singly linked list.

        Uses a two-pointer approach with a dummy node to simplify edge cases.
        First pointer advances `n` steps. Then both pointers move together until
        the first reaches the end. The second pointer will be just before the target node.

        Args:
            head (Optional[ListNode]): Head of the linked list.
            n (int): The position from the end of the list of the node to remove.

        Returns:
            Optional[ListNode]: Head of the modified list.
        """
        dummy = ListNode(0)
        dummy.next = head

        first = dummy
        second = dummy

        for _ in range(n + 1):
            first = first.next

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next

        return dummy.next
