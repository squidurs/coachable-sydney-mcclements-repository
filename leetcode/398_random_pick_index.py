from typing import List
from collections import defaultdict
from random import choice

# TEST CASES

# 1. Distinct elements
# nums = [1, 2, 3, 4] target = 3
# Expected output: 2

# 2. All elements are the same
# nums = [1, 1, 1, 1] target = 1
# Expected output: 0, 1, 2, or 3

# 3. Duplicates of target
# nums = [1, 2, 2, 2] target = 2
# Expected output: 1, 2, or 3

# 4. Single-element list
# nums = [3], target = 3
# Expected output: 0


class Solution:

    def __init__(self, nums: List[int]):
        """
        Preprocesses the input list by storing each number's indices in a dictionary.

        Args:
            nums (List[int]): The list of numbers.
        """
        self.num_to_indices = defaultdict(list)
        for i, num in enumerate(nums):
            self.num_to_indices[num].append(i)

    def pick(self, target: int) -> int:
        """
        Returns a random index where the given target number appears.
        `target` is guaranteed to be in `nums`

        Args:
            target (int): The number to search for in the list.

        Returns:
            int: A randomly selected index where `target` appears.
        """
        return choice(self.num_to_indices[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
