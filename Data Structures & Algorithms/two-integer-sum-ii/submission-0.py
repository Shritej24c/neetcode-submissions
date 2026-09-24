class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 1 
        j = len(numbers)
        while i < j: 
            if numbers[i-1] + numbers[j-1] > target:
                j -= 1 
            elif numbers[i - 1] + numbers[j - 1] < target:
                i += 1
            else: 
                break 
        return [i , j]

        