class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize the circular queue with a fixed size k.

        Args:
            k (int): Maximum number of elements the queue can hold.
        """
        self.k = k
        self.queue = [None] * k
        self.size = 0
        self.front = 0
        self.rear = -1

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return True if successful.

        Args:
            value (int): The value to insert.

        Returns:
            bool: True if the operation is successful, False if the queue is full.
        """
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.k
        self.queue[self.rear] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return True if successful.

        Returns:
            bool: True if the operation is successful, False if the queue is empty.
        """
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.k
        self.size -= 1
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.

        Returns:
            int: The front item, or -1 if the queue is empty.
        """
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        """
        Get the last item from the queue.

        Returns:
            int: The last item, or -1 if the queue is empty.
        """
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        """
        Check whether the circular queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return self.size == 0

    def isFull(self) -> bool:
        """
        Check whether the circular queue is full.

        Returns:
            bool: True if the queue is full, False otherwise.
        """
        return self.size == self.k



# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
