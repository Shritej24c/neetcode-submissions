from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ans = True
        if set(s) != set(t):
            ans = False
        else: 
            ds = Counter(s)
            dt = Counter(t)

            for i in set(s):
                if ds[i] != dt[i]:
                    ans = False
        
        return ans

        


        


        

