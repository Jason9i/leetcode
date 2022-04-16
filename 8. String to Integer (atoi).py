class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()

        if len(s) == 0:
            return 0
        if s[0] == '-':
            sign = -1
        else:
            sign = 1

        if s[0] in '-+':
            s = s.replace(s[0], '', 1)
        ans = 0
        i = 0
        while i < len(s) and s[i].isdigit():
            ans = ans * 10 + int(s[i])
            i += 1
        return -2 ** 31 if sign * ans < -2 ** 31 else 2 ** 31 - 1 if sign * ans > 2 ** 31 - 1 else sign * ans