class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0 for a in range(n)]
        stack = [0]
        i = 1
        while i < n:

            if len(stack) > 0 and temperatures[stack[-1]] < temperatures[i]:

                result[stack[-1]] = i - stack[-1]
                stack.pop()

            else:
                stack.append(i)
                i += 1

        return result