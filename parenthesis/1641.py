class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        left = 0
        for c in s:
            if c == '(':
                left += 1
            elif c == ')':
                left -= 1
            res = max(res, left)
        return res
