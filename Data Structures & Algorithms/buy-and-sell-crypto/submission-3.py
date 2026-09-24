class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn = prices[0] 
        r = 1
        best = 0
        while r < len(prices): 
            best = max(best, prices[r] - mn)

            if prices[r] < mn: 
                mn = prices[r]

            r += 1

        return best 
        