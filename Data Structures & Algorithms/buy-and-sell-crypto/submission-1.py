class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = float('inf')
        maxProfit = 0
        for i in prices:
            if i < profit:
                profit = i
            else:
                maxProfit = max(maxProfit, i - profit)
        return maxProfit