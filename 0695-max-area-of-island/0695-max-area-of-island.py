class Solution:
    def __init__(self):
        self.count = 0
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        def dfs(i, j):
            if(i < 0 or i >= len(grid) or
               j < 0 or j >= len(grid[0]) or
               grid[i][j] != 1):
               return 
            grid[i][j] = 0
            
            self.count += 1
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        max_res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.count = 0
                    dfs(i, j)
                    max_res = max(max_res, self.count)
        return max_res
