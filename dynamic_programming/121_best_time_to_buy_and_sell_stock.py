# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Sliding Window
        
        left, right = 0, 1
        _currProfit, _maxProfit = 0, 0

        while right < len(prices):
            if prices[left] < prices[right]:
                _currProfit = prices[right] - prices[left]
                _maxProfit = max(_currProfit, _maxProfit)
            else:
                left = right
            
            right += 1

        return _maxProfit

