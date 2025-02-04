from collections import defaultdict

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        """Reorders the string `s` based on the custom character order given in `order`.

        Args:
            order (str): A string representing the desired character order.
            s (str): The input string that needs to be sorted.

        Returns:
            str: A new string where characters appear in the order defined by `order`,
                 with any remaining characters appearing in their original order.
        """

        s_char_count = defaultdict(int)
        res = []

        for char in s:
            s_char_count[char] += 1

        for char in order:
            if char in s_char_count:
                res.append(char * s_char_count[char])
                del s_char_count[char]

        for char, count in s_char_count.items():
            res.append(char * count)

        return "".join(res)
