from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        Finds a peak element in the given list of integers.
        A peak element is one that is greater than its neighbors.

        Args:
            nums (List[int]): A list of integers where at least one peak element exists.

        Returns:
            int: The index of a peak element.
        """
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1

        return left
    