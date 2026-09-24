class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        n = len(s)
        if n == 0:
            return 0

        l = []
        while i < n:
            ll = [s[i]]
            j = i + 1
            while j < n :
                if s[j] not in ll:
                    ll.append(s[j])   
                    j += 1                  
                else:
                    break 
                
            l.append(len(ll))
            i += 1
            print(ll)
        return max(l)


