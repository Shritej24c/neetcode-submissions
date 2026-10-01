from collections import Counter
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ss = set(nums)

        lcs = 0

        for i in ss: 
            if i - 1 not in ss: 
                lc = 1

                while i+1 in ss: 
                    lc += 1
                    i += 1

                lcs = max(lcs,lc)

        return lcs

        