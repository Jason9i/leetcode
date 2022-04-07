class Solution:
    def arraySign(self, nums: List[int]) -> int:
        cur = 1
        for num in nums:
            if num == 0:
                return 0
            elif num < 0:
                cur *= num
        if cur < 0:
            return -1
        else:
            return 1