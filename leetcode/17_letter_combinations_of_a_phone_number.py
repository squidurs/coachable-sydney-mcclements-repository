from typing import List
from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """Generates all possible letter combinations that the given phone number digits
        could represent.

        Args:
            digits (str): A string containing digits from '2' to '9'.

        Returns:
            List[str]: A list of all possible letter combinations.
        """
        if not digits:
            return []

        dic = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        groups = []
        for digit in digits:
            groups.append(dic[digit])

        combinations = product(*groups)

        result = []
        for combination in combinations:
            result.append("".join(combination))

        return result

    def recursiveletterCombinations(self, digits: str) -> List[str]:
        """Generates all possible letter combinations that the given phone number digits could
        represent using a recursive backtracking approach.

        Args:
            digits (str): A string containing digits from '2' to '9'.

        Returns:
            List[str]: A list of all possible letter combinations.
        """
        if not digits:
            return []

        ans, sol = [], []

        dic = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        n = len(digits)

        def backtrack(i):
            if i == n:
                ans.append(''.join(sol))
                return

            for char in dic[digits[i]]:
                sol.append(char)
                backtrack(i+1)
                sol.pop()

        backtrack(0)
        return ans



    def otherletterCombinations(self, digits: str) -> List[str]:
        """Generates all possible letter combinations that the given phone number digits could represent
        using an iterative approach.

        Args:
            digits (str): A string containing digits from '2' to '9'.

        Returns:
            List[str]: A list of all possible letter combinations.
        """

        dic = {
            "2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"],
            "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]
        }

        if digits == "":
            return []

        char_combos = [""]

        for digit in digits:
            new_combo = []
            for combo in char_combos:
                for char in dic[digit]:
                    new_combo.append(combo + char)
            char_combos = new_combo

        return char_combos
