class Solution:
    def isHappy(self, n: int) -> bool:
        Dic = {n,}
        while True:
            n = sum(int(x)**2 for x in str(n))
            if n ==1:
                return True
            if n in Dic:
                return False
            Dic.add(n)