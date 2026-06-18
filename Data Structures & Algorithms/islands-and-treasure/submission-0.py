class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row, col = len(grid), len(grid[0])

        def dfs(r, c, n):
            if (r<0 or c<0 or r>=row or c>=col or grid[r][c]==-1 or grid[r][c]<n):
                return
            
            grid[r][c] = n;

            dfs(r+1, c, n+1)
            dfs(r-1, c, n+1)
            dfs(r, c+1, n+1)
            dfs(r, c-1, n+1)
        

        for r in range(row):
            for c in range(col):
                if grid[r][c]==0:
                    dfs(r, c, 0)

        return 