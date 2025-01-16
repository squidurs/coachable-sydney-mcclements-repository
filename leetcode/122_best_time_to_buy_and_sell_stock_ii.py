from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """Calculates the maximum profit from buying and selling a stock by summing all consecutive
        price increases in the list.

        The function assumes you can buy and sell the stock multiple times, but you must sell the
        stock before buying again.

        Args:
            prices (List[int]): A list of integers representing the stock price for each day.
                                Each index corresponds to a specific day.

        Returns:
            int: The maximum profit that can be achieved.
        """

        n = len(prices)
        profit = 0

        for i in range(1, n):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]

        return profit
