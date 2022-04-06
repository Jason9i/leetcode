class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for n in range(len(nums) - 2):
            if nums[n] < nums[n + 1] + nums[n + 2]:
                return nums[n] + nums[n + 1] + nums[n + 2]
        return 0
