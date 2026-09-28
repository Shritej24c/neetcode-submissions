from collections import Counter
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []

        product = 1
        dci = defaultdict(int)

        for n in nums:
            if n != 0:
                product *= n
            dci[n] += 1
        
        if dci[0] > 0: 
            ans = [0 for k in range(len(nums))]
            if dci[0] == 1:
                ans[nums.index(0)] = product

        else:
            for i in range(len(nums)):
                ans.append(product//nums[i])

        return ans
            