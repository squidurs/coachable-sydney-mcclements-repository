class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        """
        Calculates the minimum number of parentheses needed to make the input string valid.

        A valid string has matching opening '(' and closing ')' parentheses in the correct order.

        Args:
            s (str): The input string containing only '(' and ')'.

        Returns:
            int: The minimum number of parentheses to add to make the string valid.
        """

        unmatched_left = 0  # Tracks '(' that need matching ')'
        unmatched_right = 0 # Tracks ')' that need matching '('

        for p in s:
            if p == "(":
                unmatched_left += 1
            else: # p == ")"
                unmatched_left -= 1
                if unmatched_left < 0:
                    unmatched_right += 1
                    unmatched_left = 0

        return unmatched_right + unmatched_left
