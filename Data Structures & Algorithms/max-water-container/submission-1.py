class Solution:
    def maxArea(self, heights: List[int]) -> int:
        h = heights
        n = len(h)
        vol = 0
        i = 0
        j = n -1 
        while i < j: 
            vol = max(vol, (j- i)*min(h[i], h[j]))
            if h[i] < h[j]:
                i += 1
            else:
                j -= 1

        return vol