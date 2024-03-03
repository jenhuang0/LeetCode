class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #only add open par if open < n
        #only add close par if close<open
        #valid open == close == n

        stack  = []
        ans = []

        def backtrack(openN, closeN):
            if openN == closeN ==n:
                a = ''
                for i in stack:
                    a += i
                ans.append(a)
                #ans.append("".join(stack))
            if openN < n:
                stack.append("(")
                print(stack)
                backtrack (openN+1, closeN)
                stack.pop()
                print(stack)
                
            if closeN < openN:
                stack.append(")")
                backtrack (openN, closeN+1)
                stack.pop()
            
        backtrack(0, 0)

        return ans
        