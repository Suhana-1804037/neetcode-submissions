class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                dist = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                adj[i].append((j, dist))
                adj[j].append((i, dist))
        visit, ans  = set(), 0
        pq = []
        heapq.heappush(pq, (0, 0))

        while pq:
            cost, node = heapq.heappop(pq)
            if node in visit:
                continue
            visit.add(node)

            ans+= cost
            for nei, wei in adj[node]:
                if nei not in visit:
                    heapq.heappush(pq, (wei, nei))

        return ans
