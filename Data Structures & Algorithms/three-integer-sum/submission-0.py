class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ll = []
        n = len(nums)
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j + 1, n):

                    if nums[i] + nums[j] + nums[k] == 0 and sorted([nums[i], nums[j], nums[k]]) not in ll:
                        ll.append(sorted([nums[i], nums[j], nums[k]]))
        
        return ll 

                
        