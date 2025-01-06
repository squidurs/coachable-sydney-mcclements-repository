from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Finds all unique combinations of numbers in `candidates` that sum up to the `target`.

        Each number in candidates may only be used once in a combination. The solution
        ensures that no duplicate combinations are included in the result.

        Args:
            candidates (List[int]): A list of integers representing the candidate numbers.
            target (int): The target sum to achieve with combinations of the candidate numbers.

        Returns:
            List[List[int]]: A list of unique combinations, where each combination is a list of
            integers that sum to the target.
        """

        result = []
        candidates.sort()

        def combo(start: int, cur: list, target: int) -> None:
            """
            Recursively explores combinations of numbers starting from a given index.

            Args:
                start (int): The starting index in `candidates` for this recursive call.
                cur (list): The current combination being built.
                target (int): The remaining target sum to achieve.

            Side Effects:
                Modifies the `result` list by appending valid combinations.
                """

            if target == 0:
                result.append(cur)
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > target:
                    return
                combo(i + 1, cur + [candidates[i]], target - candidates[i])

        combo(0, [], target)
        return result
