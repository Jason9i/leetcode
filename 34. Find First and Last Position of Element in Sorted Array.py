class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums)

        if target < nums[low] or target >= nums[high] or nums == [] or target != x in nums:
            return [-1, -1]

        while high >= low:
            mid = (high + low) // 2
            if nums[mid] == target:
                retrun[mid, mid + 1]
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            # The only modification I did is this part
            # When we find the target, use two pointers to find its lower bound and upper bound
            if nums[mid] == target:
                while mid - 1 >= 0 and nums[mid - 1] == target:
                    mid = mid - 1
                left = mid
                mid = l + (r - l) // 2
                while mid + 1 < len(nums) and nums[mid + 1] == target:
                    mid = mid + 1
                right = mid
                return [left, right]
            if nums[mid] < target:
                l = mid + 1
            if nums[mid] > target:
                r = mid - 1

        return [-1, -1]