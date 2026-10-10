from collections import Counter
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rw = [set() for a in range(9)]
        cl = [set() for b in range(9)]
        bx = [[set() for c in range(3)] for d in range(3)]
        ans = True

        for i in range(9):
            for j in range(9):
                b = board[i][j]


                if b != '.':
                    if b in rw[i]:
                        ans = False
                        return ans
                    else:
                        rw[i].add(b)
                    
                    if b in cl[j]:
                        ans = False
                        return ans
                    else:
                        cl[j].add(b)

                    x, y = i//3, j//3

                    if b in bx[x][y]:
                        ans = False
                        return ans
                    else:
                        bx[x][y].add(b)

        return ans

                        


