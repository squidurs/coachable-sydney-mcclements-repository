from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """Finds the duplicate number in an array using Floyd's Tortoise and Hare (cycle detection) algorithm.

        Args:
            nums (List[int]): A list of n + 1 integers where each integer is in the range [1, n].
                               There is exactly one duplicate number, but it may appear more than once.

        Returns:
            int: The duplicate number present in the array.
        """
        fast = nums[0]
        slow = nums[0]

        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if slow == fast:
                break

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
