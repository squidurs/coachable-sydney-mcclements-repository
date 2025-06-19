from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Checks if the input list contains any duplicates.

        Args:
            nums (List[int]): List of integers.

        Returns:
            bool: True if any value appears more than once, False otherwise.
        """
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False
