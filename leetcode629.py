class Solution:
    
    def kInversePairs(self, n: int, k: int) -> int:
        dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
        if k == 0:
            return 1
        
        m = 1000000007
        
        for i in range(1, n+1):
            for j in range(min(k+1, (i * (i - 1) // 2)+1)):
                if i == 1 and j == 0:
                    dp[i][j] = 1
                    break
                elif j == 0:
                    dp[i][j] = 1
                else:
                    val = (dp[i-1][j] + m - (dp[i-1][j-i] if (j-i)>=0 else 0)) % m
                    dp[i][j] = (dp[i][j-1] + val) % m

        return dp[-1][-1]