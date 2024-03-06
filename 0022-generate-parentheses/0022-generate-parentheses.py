class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #only add open when it's less than n
        #only add close when it's close< open
        ans = []
        stack = []

        def backtrack(open, close):
            
            if open == close == n:
                ans.append("".join(stack))
            if open < n:
                stack.append('(')
                backtrack(open+1, close)
                stack.pop()
            if close< open:
                stack.append(')')
                backtrack(open, close+1)
                stack.pop()
        backtrack(0,0)
        return ans

                