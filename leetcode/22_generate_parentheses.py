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

        def generate(left: int, right: int, cur: List[str]) -> None:
            """
            Helper function to recursively generate valid parentheses combinations.

            Args:
                left (int): The number of remaining left parentheses to be added.
                right (int): The number of remaining right parentheses to be added.
                cur (List[str]): The current parentheses combination being built.

            Side Effects:
                Appends valid combinations of parentheses to the result list.
            """

            if left == 0 and right == 0:
                result.append("".join(cur))
                return

            if left > 0:
                cur.append("(")
                generate(left - 1, right, cur)
                cur.pop()

            if right > left:
                cur.append(")")
                generate(left, right - 1, cur)
                cur.pop()

        generate(n, n, [])
        return result
