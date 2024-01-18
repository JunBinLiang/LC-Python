class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stk = []
        valid = [False] * len(s)
        for i in range(len(s)):
            if s[i] == '(':
                stk.append(i)
            else:
                if len(stk) > 0:
                    left_i = stk.pop()
                    valid[left_i] = True
                    valid[i] = True
                
        count = 0
        res = 0
        for i in range(len(s)):
            if valid[i]:
                count += 1
            else:
                count = 0
            res = max(res, count)
            
        return res
