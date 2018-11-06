'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
'''


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        lowest, max_profit = float('inf'), 0
        for i in prices:
            lowest = min(lowest, i)
            max_profit = max(max_profit, prices - lowest)

        return max_profit