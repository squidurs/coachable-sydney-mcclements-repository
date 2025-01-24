from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """Finds the index of a target in a rotated sorted array using binary search.

        Args:
            nums (List[int]): A rotated sorted array.
            target (int): The value to find.

        Returns:
            int: The index of the target value or -1 if the value is not found.
        """

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        pivot_idx = left
        left = 0
        right = len(nums) - 1

        if target >= nums[pivot_idx] and target <= nums[right]:
            left = pivot_idx
        else:
            right = pivot_idx - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1
