class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        cur = -1
        idx = -1
        for p in points:
            if p[0] == x or p[1] == y:
                res = abs(p[0] - x) + abs(p[1] - y)
                if cur == -1 or res < cur:
                    cur = res
                    idx = points.index(p)
        return idx
