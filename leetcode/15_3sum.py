from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    """Finds all unique triplets in the list `nums` that sum up to zero.

    The function sorts the input list, then uses a two-pointer approach to identify
    triplets with a zero sum, skipping duplicates.

    Args:
        nums (List[int]): The list of integers to search for triplets.

    Returns:
        List[List[int]]: A list of unique triplets where the sum of each triplet is zero."""
    res = []
    n = len(nums)
    nums.sort()

    for i in range(n-2):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left = i + 1
        right = n - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return res

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """Finds all unique triplets in the list `nums` that sum up to zero.

    The function sorts the input list, then uses a two-pointer approach to identify
    triplets with a zero sum, avoiding duplicates by converting results to a set.

    Args:
        nums (List[int]): The list of integers to search for triplets.

    Returns:
        List[List[int]]: A list of unique triplets where the sum of each triplet is zero."""

        nums = sorted(nums)
        result = []

        for i in range(len(nums)):
            lo = i + 1
            hi = len(nums) - 1

            if nums[i] > 0:
                break

            while lo < hi:
                cur_sum = nums[i] + nums[lo] + nums[hi]

                if cur_sum < 0:
                    lo += 1

                elif cur_sum > 0:
                    hi -= 1

                else:
                    result.append([nums[i], nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1

        unique_triplets = list(set(tuple(triplet) for triplet in result))
        return [list(triplet) for triplet in unique_triplets]
