class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n-1
        
        mn= min(nums[l], nums[r])
        while l < r : 
            m = (l+r)//2
            mn = min(nums[l], nums[r])
            if nums[m] < nums[r]:
                r = m 
            else:
                l = m +1 
        return mn        
