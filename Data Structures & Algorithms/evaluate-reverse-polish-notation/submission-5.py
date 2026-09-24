class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def opp(n1, n2, op):
            if op == '+':
                return n1+n2
            elif op == '-':
                return n1-n2
            elif op == '*':
                return n1*n2
            else:
                return n1/n2

        t = []
        ops = ['+', '-', '*', '/']
        for i in range(len(tokens)):
            if tokens[i] not in ops:
                t.append(tokens[i])
            else:
                if len(t) < 2:
                    print("Error in RPN list")
                else:
                    x1 = int(t.pop(-2))
                    x2 = int(t.pop(-1))
                    n = opp(x1, x2, tokens[i])
                    print(n)
                    t.append(n)

        return int(t[0])
