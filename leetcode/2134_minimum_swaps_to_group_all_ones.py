from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        """Determines the minimum number of swaps needed to group all 1's together
        in a circular binary array using a sliding window approach.

        Args:
            nums (List[int]): A circular list of binary integers (0 and 1).

        Returns:
            int: The minimum number of swaps required to group all 1's together.
        """

        total_ones = nums.count(1)
        zeros = 0

        nums.extend(nums)
        n = len(nums)

        for i in range(total_ones):
            if nums[i] == 0:
                zeros += 1

        min_swaps = zeros

        for i in range(total_ones, n):
            if nums[i - total_ones] == 0:
                zeros -= 1

            if nums[i] == 0:
                zeros += 1

            min_swaps = min(min_swaps, zeros)

        return min_swaps
