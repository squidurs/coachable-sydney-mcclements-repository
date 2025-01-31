class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """Removes the minimum number of parentheses to make the input string valid.

        Args:
            s (str): A string containing parentheses to be validated.

        Returns:
            str: The string with the minimum number of parentheses removed to make it valid.
        """

        str_builder = []
        left_parentheses_count = 0

        for char in s:
            if char == "(":
                left_parentheses_count += 1
                str_builder.append(char)
            elif char == ")":
                if left_parentheses_count > 0:
                    left_parentheses_count -= 1
                    str_builder.append(char)
            else:
                str_builder.append(char)

        if left_parentheses_count ==  0:
            return ''.join(str_builder)

        res_builder = []
        for char in reversed(str_builder):
            if char == "(" and left_parentheses_count > 0:
                left_parentheses_count -= 1
            else:
                res_builder.append(char)

        return ''.join(reversed(res_builder))
