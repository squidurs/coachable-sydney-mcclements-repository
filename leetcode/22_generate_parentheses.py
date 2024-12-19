from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Generates all combinations of well-formed parentheses for a given number of pairs.

        Args:
            n (int): The number of pairs of parentheses.

        Returns:
            List[str]: A list of all valid combinations of well-formed parentheses.
        """

        result = []

        def generate(open: int, close: int, cur: List[str]) -> None:
            """
            Helper function to recursively generate valid parentheses combinations.

            Args:
                open (int): The number of remaining open parentheses to be added.
                close (int): The number of remaining close parentheses to be added.
                cur (List[str]): The current parentheses combination being built.
            """

            if open == 0 and close == 0:
                result.append("".join(cur))
                return

            if open > 0:
                cur.append("(")
                generate(open - 1, close, cur)
                cur.pop()

            if close > open:
                cur.append(")")
                generate(open, close - 1, cur)
                cur.pop()

        generate(n, n, [])
        return result
    
