class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        sdic = set()
        for i in range(n):
            if i > k:
                sdic.remove(nums[i-k-1])
                
            if nums[i] in sdic:
                return True
            
            sdic.add(nums[i] )

        return False



            
            