from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Finds the majority element in a list, which is the element that appears more than n // 2 times.
        This solution assumes a majority element exists in nums.

        This uses the Boyer-Moore Voting Algorithm, which allows finding the majority element in O(n)
        time with O(1) space.

        Args:
            nums (List[int]): The list of integers.

        Returns:
            int: The majority element in the list.
        """
        majority_el = None
        count = 0

        for num in nums:
            if count == 0:
                majority_el = num
            count += (1 if num == majority_el else -1)

        return majority_el