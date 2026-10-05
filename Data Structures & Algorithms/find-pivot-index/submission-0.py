class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lsum = [0]
        rsum = [0]
        ans = -1 
        for i in range(1, len(nums)):

            lsum.append(lsum[i-1] + nums[i-1])
            rsum.append(rsum[i-1] + nums[-i])

        rsum = rsum[::-1]

        for i in range(len(nums)):
            if lsum[i] == rsum[i]:
                ans = i
                break 

        return ans