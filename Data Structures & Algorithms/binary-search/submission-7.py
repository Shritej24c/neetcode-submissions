class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lf = 0
        rg = len(nums) -1
        def search_bs(nums, l, r):

            m = (l+r)//2
            print(m)

            if target == nums[m]:
                return m
            elif l == r:
                return -1
            elif target > nums[m]:
                return search_bs(nums, m + 1, r)
            elif target < nums[m]:
                return search_bs(nums, l, m)
            
        
        return search_bs(nums, lf, rg)