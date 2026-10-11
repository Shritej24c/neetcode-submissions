class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = []
        i = -1
        maxi = -1
        while i > -n- 1:
            e = temperatures[i]
            maxm = temperatures[maxi]

            if e >= maxm:
                maxi = i
                result.append(0)
            else:
                j = i + 1
                while j <= maxi:
                    if temperatures[i] < temperatures[j]:
                        result.append(j-i)
                        break
                    
                    j += 1


            i -= 1
        
        return result[::-1]





        
                
