class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        
        nums = candidates[:]
        nums.sort()
        
        def backtrack(i, cur_path, cur_sum):
            if cur_sum == target:
                ans.append(cur_path[::])
                return
            if cur_sum > target:
                return
            
            if i >= len(nums):
                return
            
            cur_path.append(nums[i])
            cur_sum += nums[i]
            
            backtrack(i+1, cur_path, cur_sum)
            
            cur_path.pop()
            cur_sum -= nums[i]
            
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            
            backtrack(i+1, cur_path, cur_sum)
        
        backtrack(0, [], 0)
        return ans
            
            