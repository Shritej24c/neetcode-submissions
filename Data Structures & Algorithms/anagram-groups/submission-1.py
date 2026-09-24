from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dci = {}
        
        for ss in strs: 
            dci[ss] = Counter(ss)
    
        final = []
        l = len(strs)
        i = 0
        while l > 0: 
            c = [strs[i]]
            el_rm = [strs[i]]
            for j in range(i+1, len(strs)):
                if dci[strs[i]] == dci[strs[j]]:
                    c.append(strs[j])
                    el_rm.append(strs[j])

            strs = [i for i in strs if i not in el_rm]
            l = len(strs)
            final.append(c)

        return final
                    


            
                

