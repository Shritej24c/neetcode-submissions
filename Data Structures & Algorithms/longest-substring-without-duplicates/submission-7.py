class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        n = len(s)
        if n == 0:
            return 0
        l = 1
        while i < n:
            j = i + l + 1 
            while j <= n:
                if len(set(s[i: j])) == len(s[i:j]):
                    l = len(s[i:j])
                    j += 1
                else: 
                    break 
            
            i += 1

        return l



# while j < n :
            #     if s[j] not in ll:
            #         ll.append(s[j])   
            #         j += 1                  
            #     else:
            #         break 

