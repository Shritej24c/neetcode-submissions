class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n-1
        
        mn= min(nums[l], nums[r])
        while l < r: 
            m = (l+r)//2
            mn = min(nums[l], nums[r])
            if nums[l] < min(nums[r], nums[m]) or nums[m] < mn:
                r = m 
            elif nums[r] < min(nums[m], nums[l]):
                l = m +1
            elif r - l == 1: 
                mn = min(nums[l], nums[r])
                break
        return mn        
