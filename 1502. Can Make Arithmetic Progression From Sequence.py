class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[0] - arr[1]
        for idx in range(len(arr) - 1):
            res = arr[idx] - arr[idx + 1]
            if diff != res:
                return False
        return True
