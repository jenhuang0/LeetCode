class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        target_len = len(nums)
        ans = []
        arr = deque(nums)
        def dfs(arr, cur_path):
            if len(cur_path) == target_len:
                return cur_path[:]
            
            for i in range(len(arr)):
                first = arr.popleft()
                cur_path.append(first)

                new = dfs(arr, cur_path)
                if new:
                    ans.append(dfs(arr, cur_path))

                cur_path.pop()
                arr.append(first)
            
            
            
        dfs(arr, [])
    
        return ans