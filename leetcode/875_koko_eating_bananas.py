from typing import List
from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Determines the minimum eating speed `k` (in bananas per hour) such that all piles
        of bananas can be eaten within `h` hours.

        This method uses binary search to find the optimal `k`. The goal is to minimize
        `k` while ensuring that all piles can be consumed within the time constraint.

        Args:
            piles (List[int]): A list of integers representing the number of bananas in each pile.
            h (int): The number of hours available to eat all the bananas.

        Returns:
            int: The minimum integer `k` representing the eating speed in bananas per hour.
        """

        def k_works(k):
            """
            Checks if a given eating speed `k` allows all the piles to be eaten within `h` hours.

            Args:
                k (int): The eating speed in bananas per hour.

            Returns:
                bool: `True` if the eating speed `k` allows completing all piles within `h` hours;
                `False` otherwise.
            """
            hours = 0
            for p in piles:
                hours += ceil(p/k)
            return hours <= h

        lo = 1
        hi = max(piles)

        while lo < hi:
            k = (lo + hi) // 2
            if k_works(k):
                hi = k
            else:
                lo = k + 1

        return lo
    