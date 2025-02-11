class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        Computes x raised to the power n using exponentiation by squaring.

        Args:
            x (float): The base.
            n (int): The exponent (may be negative)

        Returns:
            float: The computed power.
        """
        if x == 0:
            return 0

        if n < 0:
            x = 1 / x
            n = -n

        result = 1.0

        while n:
            # If n is odd, multiply result by x.
            if n % 2 == 1:
                result *= x

            x *= x
            n //= 2

        return result

    def myPow2(self, x: float, n: int) -> float:
        """
        Computes x raised to the power n using exponentiation by squaring.

        Args:
            x (float): The base.
            n (int): The exponent (may be negative)

        Returns:
            float: The computed power.
        """
        def fast_power(base: float, exponent: int) -> float:
            """
            Recursively computes the power using exponentiation by squaring.

            Args:
                base (float): The base.
                exponent (int): The exponent (positive integer)

            Returns:
                float: base raised to the power of exponent.
            """
            if base == 0:
                return 0
            if exponent == 0:
                return 1

            # Recursively compute half power.
            res = fast_power(base * base, exponent//2)
            # If exponent is odd, multiply by base one extra time.
            return base * res if exponent % 2 else res

        result = fast_power(x, abs(n))

        if n < 0:
            return 1 / result
        return result
