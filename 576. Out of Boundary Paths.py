class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        memo = [[[-1 for i in range(maxMove+1)] for _ in range(n)] for _ in range(m)]
        mod = 1000000007
        
        def dfs(r, c, M):
            if 0 > r or r >= m or c >= n or c < 0:
                return 1
            
            if M == 0:
                return 0
            
            if memo[r][c][M] >= 0:
                return memo[r][c][M]
            
            memo[r][c][M] = ((dfs(r+1, c, M-1) + dfs(r-1, c, M-1))%mod + (dfs(r, c+1, M-1) + dfs(r, c-1, M-1))%mod)%mod
            return memo[r][c][M]
        
        return dfs(startRow, startColumn, maxMove)