class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low = 1
        high = num
        while high >= low:
            mid = (high + low) // 2
            if mid ** 2 == num:
                return True
            elif mid ** 2 > num:
                high = mid - 1
            elif mid ** 2 < num:
                low = mid + 1
        return False
