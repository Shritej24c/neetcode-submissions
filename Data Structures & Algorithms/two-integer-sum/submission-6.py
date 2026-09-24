class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dci = {}
        for i in range(len(nums)):
            if nums[i] in dci: 
            # dci[nums[i]][0] == target - nums[i]:
                return [dci[nums[i]], i]
            
            dci[target - nums[i]] = i
