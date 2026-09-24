class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = ''.join([i.lower() for i in s if i.isalnum()])

        i = 0 
        j = len(ss) - 1
        aa = True
        while i < j: 
            if ss[i] != ss[j]:
                aa = False
            i += 1
            j -= 1
        
        return aa