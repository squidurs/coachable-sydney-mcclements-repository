class Solution:
    def numSquares(self, n: int) -> int:
        """
        Finds the minimum number of perfect square numbers that sum up to n

        Args:
            n (int): The target number.

        Returns:
            int: The minimum number of perfect squares that sum up to n.
        """
        squares = []
        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1

        dp = [n] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for square in squares:
                if square > i:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)

        return dp[n]
