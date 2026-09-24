class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0 , len(heights) - 1
        # w = 0
        h = heights[0]
        w = 0

        while l < r: 
            if heights[l] < heights[r]:
                
                w = max(w, (r - l)*heights[l])
                l += 1
            else:
                w = max(w, (r - l)*heights[r])
                r -= 1

        return w
