class Solution:
    def countOdds(self, low: int, high: int) -> int:
        diff = high - low
        return diff//2 + 1 if high%2 or low%2 else diff//2