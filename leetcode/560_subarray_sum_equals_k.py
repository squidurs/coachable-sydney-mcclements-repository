from typing import List
from collections import defaultdict

def subarraySum(nums: List[int], k: int) -> int:
    """
    Finds the total number of subarrays whose sum equals k

    Args:
        nums (List[int]): List of integers.
        k (int): The target sum for subarrays.

    Returns:
        int: The count of subarrays whose sum equals k
    """
    total = 0
    prefix_counts = defaultdict(int)
    prefix_counts[0] = 1
    running_sum = 0

    for num in nums:
        running_sum += num
        total += prefix_counts[running_sum - k]
        prefix_counts[running_sum] += 1

    return total