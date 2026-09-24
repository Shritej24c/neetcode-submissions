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
                if len(ln) == 0 or i != dci[ln.pop()] :
                    ans = False
                    break
        if len(ln) != 0:
            ans = False
        
        return ans
            