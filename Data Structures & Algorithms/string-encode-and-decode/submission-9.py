class Solution:

    def encode(self, strs: List[str]) -> str:
        en_str = ''
        for s in strs:
            l = len(s)
            if l < 10:
                en_str += '<'
            elif l >= 10 and l < 100:
                en_str += '>'
            else:
                en_str += '?'

            en_str += str(l)
            en_str += s
        print(en_str)
        return en_str
        

    def decode(self, s: str) -> List[str]:
        n = len(s)
        n_lst = []
        i = 0 
        ee = 0
        while i < n:
            if s[i] == '<':
                ee = 0
            elif s[i] == '>':
                ee = 1
            elif s[i] == '?':
                ee = 2

            print(s[i+1: i+2+ee])   

            l_str = int(s[i+1: i+2+ee])
            
            if i+2+ee+l_str >= n:
                n_lst.append(s[i+2+ee:])
            else:
                n_lst.append(s[i+2+ee:i+2+ee+l_str])

            i += 2+ee+l_str
        
        return n_lst


