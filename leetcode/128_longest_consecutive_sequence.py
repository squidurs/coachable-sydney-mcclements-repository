from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """Finds the length of the longest consecutive sequence in an unsorted list of integers.

        Args:
            nums (List[int]): A list of integers.

        Returns:
            int: The length of the longest consecutive sequence of integers.
        """

        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:
                length = 1
                next_num = num + 1

                while next_num in num_set:
                    length += 1
                    next_num += 1
                longest = max(length, longest)

        return longest
