class Solution:
    def reverse(self, x: int) -> int:
        """
        Reverses the digits of a given signed 32-bit integer `x`.

        Args:
            x (int): The integer to be reversed.

        Returns:
            int: The reversed integer if it does not overflow 32-bit signed integer bounds.
                 Returns 0 if the reversed integer overflows.
        """

        reverse_number = 0
        abs_x = abs(x)
        max_int = 2**31 - 1

        while abs_x != 0:
            digit = abs_x % 10
            if reverse_number > (max_int // 10) or (reverse_number == (max_int // 10) and digit > 7):
                return 0
            reverse_number = reverse_number * 10 + digit
            abs_x //= 10

        return reverse_number if x > 0 else -reverse_number