class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        num = 1
        while num ** 2 <= x:
            low = num
            num *= 2
        high = num

        while high >= low:
            mid = (high + low) // 2
            if mid ** 2 == x:
                return mid
            elif mid ** 2 > x:
                high = mid - 1
            else:
                low = mid + 1
        return high