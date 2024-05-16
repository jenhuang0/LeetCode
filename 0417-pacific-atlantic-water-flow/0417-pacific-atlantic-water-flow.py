class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # use two set to store the cell can reach pacific ocean and atlantic ocean
        # can get the cell can reach both in both sets

        ROWS, COLS = len(heights), len(heights[0])
        alt = set()
        pac = set()
        
        def dfs(r, c, visit, prevHeight):
            dire = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            if (r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                (r, c) in visit or
                heights[r][c] < prevHeight):
                return
            visit.add((r,c))
            for dr, dc in dire:
                dfs(r + dr, c + dc, visit, heights[r][c])
            
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, alt, heights[ROWS - 1][c])
        
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, alt, heights[r][COLS - 1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in alt and (r, c) in pac:
                    res.append([r, c])
        return res

            