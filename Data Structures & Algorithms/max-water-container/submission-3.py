class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lp = 0
        rp = len(heights) - 1
        amt_wtr = 0

        while lp < rp:
            low_val = min(heights[lp], heights[rp])

            amt_wtr = max(amt_wtr, low_val*(rp - lp))

            if heights[lp] < heights[rp]:
                lp += 1
            else:
                rp -= 1
            
        return amt_wtr

        
