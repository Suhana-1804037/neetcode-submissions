class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        directions = [[1,0], [-1,0], [0, 1], [0, -1]]
        row, col = len(grid), len(grid[0])
        ans, visit = 0, set()

        def bfs(r, c):
            q = deque()
            grid[r][c] = "0"
            q.append((r,c))

            while q:
                rw, cl = q.popleft()
                for dr, dc in directions:
                    r, c = dr+rw, dc+cl
                    if (r<0 or c<0 or r>=row or c>=col or grid[r][c]=="0"):
                        continue
                    q.append((r, c))
                    grid[r][c] = "0"


        for r in range(row):
            for c in range(col):
                if grid[r][c]=="1" and (r, c) not in visit:
                    bfs(r, c)
                    ans+=1
        return ans