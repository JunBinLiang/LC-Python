class Solution:
    def minInsertions(self, s: str) -> int:
        left = 0
        answer = 0
        
        n = len(s)
        i = 0
        while i < n:
            if s[i] == '(':
                left += 1
                i += 1
            else:
                if i + 1 < n and s[i + 1] == ')':
                    if left == 0:
                        answer += 1
                        i += 2
                    else:
                        left -= 1
                        i += 2
                else:
                    if left == 0:
                        answer += 2
                        i += 1
                    else:
                        answer += 1
                        i += 1
                        left -= 1
        return answer + left * 2
