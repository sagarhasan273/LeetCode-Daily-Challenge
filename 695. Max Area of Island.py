class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = [0, 0]
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c):
            if 0 <= r < rows and 0 <= c < cols:
                if grid[r][c] == 1:
                    grid[r][c] = 2
                    maxArea[1] += 1
                    maxArea[0] = max(maxArea[0], maxArea[1])
                    for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                        dfs(r+dr, c+dc)
                    
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxArea[1] = 0
                    dfs(r, c)
        
        return maxArea[0]