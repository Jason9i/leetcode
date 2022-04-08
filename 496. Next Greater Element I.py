class Solution:
    def nextGreaterElement(self, A: List[int], B: List[int]) -> List[int]:
        stack = []
        diff = {}

        for pos, val in enumerate(B):

            while stack and stack[-1] < val:
                diff[stack.pop()] = val

            stack.append(val)

        for pos in range(len(A)):

            if A[pos] in diff:
                A[pos] = diff[A[pos]]
            else:
                A[pos] = -1

        return A
