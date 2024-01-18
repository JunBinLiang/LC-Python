class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def recursion(left, right, s):
            #base case
            if left + right == 2 * n:
                if left == right:#valid
                    ans.append(s) 
                return
            
            recursion(left + 1, right, s + '(')
            if left - right > 0:
                recursion(left, right + 1, s + ')')
                
        recursion(0, 0, "")
        return ans
