class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum = 0
        pro = 1
        while n:
            res = n%10
            sum += res
            pro *= res
            n = n//10
        return pro - sum