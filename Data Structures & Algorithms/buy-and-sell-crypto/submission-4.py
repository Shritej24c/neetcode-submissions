class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        lb = 0
        hs = 1
        while hs < len(prices):
            if prices[hs] < prices[lb]:
                lb = hs

            else:
                profit = max(profit, prices[hs] - prices[lb])

                hs += 1
                
        return profit



