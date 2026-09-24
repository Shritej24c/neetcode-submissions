class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dci = {}
        for i in nums: 
            if i not in dci:
                dci[i] = 1
            else: 
                return True
        return False 