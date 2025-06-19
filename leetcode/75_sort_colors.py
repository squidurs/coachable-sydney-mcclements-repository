from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Sorts an array containing only 0s, 1s, and 2s in-place.

        This uses a three-pointer approach:
        - 'low' tracks the boundary of 0s (start of the list),
        - 'mid' scans through the list,
        - 'high' tracks the boundary of 2s (end of the list).

        The algorithm places all 0s before 'low', all 2s after 'high',
        and all 1s in between, by swapping values as needed while
        maintaining the three regions.

        Args:
            nums (List[int]): A list containing only 0s, 1s, and 2s.
        """
        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
