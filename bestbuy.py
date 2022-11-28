class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = 0
        sell = 1
        while sell<len(prices):
            currentProfit = prices[sell] - prices[buy]
            if(prices[buy] < prices[sell]):
                profit = max(profit, currentProfit)
            else:
                buy = sell
            sell += 1
        
        return profit
