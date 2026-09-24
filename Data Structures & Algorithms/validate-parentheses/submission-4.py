class Solution:
    def isValid(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        dci = {'(':")", '{': '}', '[': ']'}
        ans = True
        ln = []
        for i in s:
            if i in dci:
                ln.append(i)
            else:
                if len(ln) == 0 or i != dci[ln[-1]] :
                    ans = False
                    break
                else: 
                    ln = ln[:-1]
        if len(ln) != 0:
            ans = False
        
        return ans
            