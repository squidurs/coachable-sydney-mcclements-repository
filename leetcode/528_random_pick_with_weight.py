from typing import List
import random

class Solution:
    """
    A solution to randomly pick an index based on weighted probabilities.
    """
    def __init__(self, w: List[int]):
        """
        Initializes the Solution object with weights.

        Args:
            w (List[int]): A list of positive integers representing weights.
        """

        total = 0
        self.prefix_sum = []

        for weight in w:
            total += weight
            self.prefix_sum.append(total)

        self.total = total


    def pickIndex(self) -> int:
        """
        Randomly picks an index based on weighted probabilities.

        Returns:
            int: The randomly selected index.
        """
        target = random.uniform(0, self.total)

        left = 0
        right = len(self.prefix_sum)

        while left < right:
            mid = (left + right)//2

            if self.prefix_sum[mid] < target:
                left = mid + 1
            else:
                right = mid

        return left


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
