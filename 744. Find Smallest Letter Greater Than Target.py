class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low = 0
        high = len(letters) - 1

        if letters[low] > target or letters[high] <= target:
            return letters[low]

        while high >= low:
            mid = low + (high - low) // 2
            if letters[mid] <= target:
                low = mid + 1
            elif letters[mid] > target:
                high = mid - 1
        return letters[low]