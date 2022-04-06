class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        res = 0
        for set1 in arr1:
            for set2 in arr2:
                if abs(set1 - set2) <= d:
                    break
            else: res += 1
        return res