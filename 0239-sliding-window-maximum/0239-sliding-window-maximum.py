class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        ans = []
        max_stack = deque()

        for i in range(len(nums)):
            #maintain the que in decreasing order
            while max_stack and max_stack[-1]<nums[i]:
                max_stack.pop()
            max_stack.append(i)
            #ensure queue is only holding the index of current window
            if max_stack[0] <= i - k:
                max_stack.popleft
            if i>=k-1:
                ans.append(nums[max_stack[0]])

        return ans



