from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Removes all instances of `val` from the list in-place and returns the new length of the list.

        The list is modified such that the elements that are not `val` are moved to the front.

        Args:
            nums (List[int]): The list of integers.
            val (int): The value to remove from the list.

        Returns:
            int: The new length of the list after removal.
        """
        k = 0

        for i, num in enumerate(nums):
            if num != val:
                nums[k], nums[i] = nums[i], nums[k]
                k += 1

        return k
