from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """Calculates the maximum profit from buying and selling a stock by identifying all
        peaks and valleys in the price array.

        The function assumes you can buy and sell the stock multiple times, but you must sell the
        stock before buying again.

        Args:
            prices (List[int]): A list of integers representing the stock price for each day.
                                Each index corresponds to a specific day.

        Returns:
            int: The maximum profit that can be achieved by summing the differences
                 between all peaks and valleys.
        """

        n = len(prices)
        lo = prices[0]
        hi = prices[0]
        profit = 0
        i = 0

        while i < n - 1:
            while i < n - 1 and prices[i] >= prices[i+1]:
                i += 1
            lo = prices[i]

            while i < n - 1 and prices[i] <= prices[i+1]:
                i += 1
            hi = prices[i]
            profit += hi - lo

        return profit