from typing import List
from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Generates all possible letter combinations for the given digits using recursion,
        without a helper function and with direct string concatenation.

        Args:
            digits (str): A string containing digits from '2' to '9'.

        Returns:
            List[str]: A list of all possible letter combinations.
        """
        if not digits:
            return []

        digit_to_letters_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        if len(digits) == 1:
            return list(digit_to_letters_map[digits])

        # Build combinations recursively by appending each letter of the current digit
        # to all combinations generated from the previous digits.
        previous_combinations = self.letterCombinations(digits[:-1])
        current_digit_letters = digit_to_letters_map[digits[-1]]

        res = []

        for combo in previous_combinations:
            for letter in current_digit_letters:
                res.append(combo + letter)

        return res

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

        digit_to_letter_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        groups = []
        for digit in digits:
            groups.append(digit_to_letter_map[digit])

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

        total_combinations, cur_combination = [], []

        digit_to_letter_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        n = len(digits)

        def backtrack(i: int) -> None:
            if i == n:
                total_combinations.append(''.join(cur_combination))
                return

            for char in digit_to_letter_map[digits[i]]:
                cur_combination.append(char)
                backtrack(i+1)
                cur_combination.pop()

        backtrack(0)
        return total_combinations



    def otherletterCombinations(self, digits: str) -> List[str]:
        """Generates all possible letter combinations that the given phone number digits could represent
        using an iterative approach.

        Args:
            digits (str): A string containing digits from '2' to '9'.

        Returns:
            List[str]: A list of all possible letter combinations.
        """

        digit_to_letters_map = {
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
                for char in digit_to_letters_map[digit]:
                    new_combo.append(combo + char)
            char_combos = new_combo

        return char_combos
