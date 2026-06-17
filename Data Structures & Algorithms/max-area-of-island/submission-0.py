class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        ans = 0
        directions = [[1,0],[-1,0],[0,1],[0,-1]]


        def bfs(rr, cc):
            mxIsland = 0
            q = deque()
            grid[rr][cc]=0
            q.append((rr,cc))
            
            while q:
                rq, cq = q.popleft()
                mxIsland+=1
                for dr, dc in directions:
                    r, c = rq+dr, cq+dc
                    if (r<0 or c<0 or r>=row or c>=col or grid[r][c]==0):
                        continue
                    q.append((r,c))
                    grid[r][c]=0
            return mxIsland



        for r in range(row):
            for c in range(col):
                if grid[r][c]==1:
                    ans = max(ans, bfs(r,c))
        
        return ans