class Node:
    def __init__(self, val: int, next: 'Node' = None):
        """
        Definition for a Node.

        Args:
            x (int): The value of the node.
            next (Node, optional): Reference to the next node in the list.
        """
        self.val = val
        self.next = next

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        """
        Inserts a new node with value 'insertVal' into the circular sorted linked list.

        Args:
            head (Node): The head of the circular linked list.
            insertVal (int): The value to insert.

        Returns:
            Node: The head of the updated circular linked list.
        """
        if not head:
            new_head = Node(insertVal)
            new_head.next = new_head
            return new_head

        cur = head

        while True:
            if cur.val <= insertVal < cur.next.val:
                break
            # turning point (max -> min)
            if cur.val > cur.next.val:
                if insertVal >= cur.val or insertVal <= cur.next.val:
                    break

            cur = cur.next
            # cycle complete
            if cur == head:
                break

        new_node = Node(insertVal, cur.next)
        cur.next = new_node
        return head



class Solution2:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        """
        Inserts a new node with value 'insertVal' into the circular sorted linked list.

        Args:
            head (Node): The head of the circular linked list.
            insertVal (int): The value to insert.

        Returns:
            Node: The head of the updated circular linked list.
        """

        if not head:
            new_head = Node(insertVal)
            new_head.next = new_head
            return new_head

        cur = head

        while cur.next != head:
            if cur.val <= insertVal < cur.next.val:
                new_node = Node(insertVal, cur.next)
                cur.next = new_node
                return head
            if cur.val > cur.next.val: # current is the max value and next is the min
                if insertVal >= cur.val or insertVal <= cur.next.val:
                    new_node = Node(insertVal, cur.next)
                    cur.next = new_node
                    return head
            cur = cur.next

        # cycle complete. head >= insertVal >= last element in the cycle
        new_node = Node(insertVal, cur.next)
        cur.next = new_node
        return head
