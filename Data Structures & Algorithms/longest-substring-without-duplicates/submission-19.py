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
                    prev = ss[s[r]]
                    i = prev + 1
                    if r - prev  == 1:
                        r = i + 1
                        
                    ss[s[i]] = i
                else:
                    ss[s[r]] = r
                    r += 1
            lsc = max(lsc, r - i)
        return lsc
                


            
            
