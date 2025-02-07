class MinStack:
    """
    MinStack provides a stack data structure with constant-time operations
    to push, pop, peek (top), and retrieve the minimum element (getMin).
    """

    def __init__(self):
        """
        Initializes an empty MinStack with two stacks:
        - 'stack' for storing values in LIFO order.
        - 'min_stack' for tracking the minimum value at each level of the stack.
        """
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        """
        Pushes a value onto the stack and updates the minimum stack.

        Args:
            val (int): The value to be pushed onto the stack.
        """
        self.stack.append(val)
        val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(val)

    def pop(self) -> None:
        """
        Removes the top element from both the value stack and the minimum stack.
        """
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        """
        Retrieves the top element of the stack without removing it.

        Returns:
            int: The top value of the stack.
        """
        return self.stack[-1]

    def getMin(self) -> int:
        """
        Retrieves the minimum element in the stack wihout removing it.

        Returns:
            int: The current minimum value in the stack.
        """
        return self.min_stack[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
