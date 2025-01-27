class Solution:

    def calculate(self, s: str) -> int:
        """Evaluates a mathematical expression given as a string using a stack.

        Args:
            s (str): A string containing the mathematical expression.

        Returns:
            int: The result of evaluating the expression.
        """

        digits = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        integer = 0
        stack = []
        i = 0
        current_operator = '+'

        while i < len(s):
            cur_char = s[i]
            if cur_char in digits:
                integer = (integer * 10) + digits[cur_char]
            if cur_char in '+-*/' or i == len(s) - 1:
                if current_operator == '+':
                    stack.append(integer)
                elif current_operator == '-':
                    stack.append(-integer)
                elif current_operator == '*':
                    stack[-1] *= integer
                elif current_operator == '/':
                    stack[-1] //= integer
                current_operator = cur_char
                integer = 0
            i += 1

        return sum(stack)


    def calculate(self, s: str) -> int:
        """Evaluates a mathematical expression in a string with constant space complexity.

        Args:
            s (str): A string containing the mathematical expression.

        Returns:
            int: The result of evaluating the expression.
        """

        digits = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        cur_num = 0
        prev_num = 0
        res = 0
        i = 0
        current_operator = '+'

        while i < len(s):
            cur_char = s[i]

            if cur_char in digits:
                cur_num = 0
                while i < len(s) and s[i] in digits:
                    cur_num = (cur_num * 10) + digits[s[i]]
                    i += 1
                if current_operator == '+':
                    res += cur_num
                    prev_num = cur_num
                elif current_operator == '-':
                    res -= cur_num
                    prev_num = -cur_num
                elif current_operator == '*':
                    res -= prev_num
                    res += (prev_num * cur_num)
                    prev_num = prev_num * cur_num
                elif current_operator == '/':
                    res -= prev_num
                    res += int(prev_num / cur_num)
                    prev_num = int(prev_num / cur_num)
                continue
            elif cur_char != ' ':
                current_operator = cur_char
            i += 1

        return res
