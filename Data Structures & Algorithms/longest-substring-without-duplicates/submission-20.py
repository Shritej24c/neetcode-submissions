class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        

        if n == 0:
            return 0 
        else :
            i = 0 
            lsc = r = 1
            ss = dict()
            ss[s[i]] = i
            while r < n: 
                if ss.get(s[r], -1) >= i:
                    lsc = max(lsc, r - i)
                    i = ss[s[r]] + 1

                    ss[s[r]] = r
                else:
                    ss[s[r]] = r
                r += 1
            lsc = max(lsc, r - i)
        return lsc
                


            
            
