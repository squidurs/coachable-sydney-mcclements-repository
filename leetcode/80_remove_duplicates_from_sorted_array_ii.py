from typing import List

def removeDuplicates(self, nums: List[int]) -> int:
    """Removes duplicates from a sorted list such that each element appears at most twice.

    Args:
        nums (List[int]): A list of integers sorted in non-decreasing order.

    Returns:
        int: The length of the list after removing extra duplicates.
    """
    if len(nums) <= 2:
        return len(nums)

    i = 2

    for j in range(2, len(nums)):
        if nums[j] != nums[i-2]:
            nums[i] = nums[j]
            i += 1

    return i