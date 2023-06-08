# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left, right = 0, 1
        _maxProfit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                _maxProfit += prices[right] - prices[left]
            
            left = right
            right += 1

        return _maxProfit
