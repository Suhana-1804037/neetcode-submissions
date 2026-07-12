class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n, visit = len(grid), set()
        pq = []
        heapq.heappush(pq, [grid[0][0], 0, 0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visit.add((0, 0))
        while pq:
            t, r, c = heapq.heappop(pq)
            if r==n-1 and c==n-1:
                return t
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if (nr<0 or nc<0 or nr>=n or nc>=n or (nr, nc) in visit):
                    continue
                visit.add((nr, nc))
                heapq.heappush(pq, [max(t, grid[nr][nc]), nr, nc])
