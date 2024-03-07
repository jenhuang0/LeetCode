class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        # stack is to record in decreasing order
        ans = [0]*len(t)
        stack = []
        
        for i in range(len(t)):
            idx = t[i]
            while len(stack)>0 and idx > t[stack[-1]]:
                ans[stack[-1]]=i - stack[-1]
                stack.pop()
            stack.append(i)
        return ans