class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[0] * n for _ in range(m)]
        #dp[m-1][n-1] = True
        
        ans = 0
        def solve(x, y):
            if x>=m or y>=n:
                return 0
            if dp[x][y]!=0:
                return dp[x][y]
            if x==m-1 and y==n-1:
                return 1
            dp[x][y] = solve(x+1, y) + solve(x, y+1)
            return dp[x][y]
        
        
        return solve(0, 0)

