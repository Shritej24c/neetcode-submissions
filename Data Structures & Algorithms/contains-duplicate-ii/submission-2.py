class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        sdic = {}
        for i in range(n):
            if i > k:
                sdic.pop(nums[i-k-1], None)
                
            if nums[i] in sdic:
                return True
            
            sdic[nums[i] ] = i

        return False



            
            