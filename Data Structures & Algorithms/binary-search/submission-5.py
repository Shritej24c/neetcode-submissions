class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = len(nums)
        mm = l//2
        ans = -1
        if len(nums) == 0:
            return -1
        elif len(nums) == 1 and target != nums[mm]:
            return -1
        elif target == nums[mm]:
            ans = mm
        elif target > nums[mm]:
            nums = nums[mm+1:]
            a = self.search(nums, target)
            if a == -1:
                ans = -1
            else:
                ans = mm + 1 + self.search(nums, target)
        else: 
            nums = nums[:mm]
            ans = self.search(nums, target)

        return ans
        