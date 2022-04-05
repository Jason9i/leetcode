class Solution:
    def hammingWeight(self, n: int) -> int:
        return '{:032b}'.format(n).count('1')


class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")
