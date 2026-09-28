from collections import Counter
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []

        pre_prod = [1]
        suf_prod = [1]

        pp = 1
        sp = 1

        rnums = nums[::-1]

        for i in range(1,len(nums)):
            pp *= nums[i-1]
            pre_prod.append(pp)


            sp *= rnums[i-1]
            suf_prod.append(sp)
        
        suf_prod = suf_prod[::-1]

        for i in range(len(nums)):
            ans.append(suf_prod[i]*pre_prod[i])

        
        return ans