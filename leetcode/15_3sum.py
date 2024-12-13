from typing import List

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

                if sum < 0:
                    lo += 1

                elif sum > 0:
                    hi -= 1

                else:
                    result.append([nums[i], nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1

        unique_triplets = list(set(tuple(triplet) for triplet in result))
        return [list(triplet) for triplet in unique_triplets]
    