class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if sorted(s1) != sorted(s2):
            return False
        c = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                c += 1

        if c > 2:
            return False
        return True


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        cnt = 0
        diff1 = []
        diff2 = []
        for idx in range(len(s1)):
            if s1[idx] != s2[idx]:
                cnt += 1
                diff1.append(s1[idx])
                diff2.append(s2[idx])

        if cnt > 2:
            return False
        elif sorted(diff1) != sorted(diff2):
            return False
        return True
