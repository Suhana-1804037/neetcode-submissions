class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        visit, ans = set(), 0
        
        for u, v, w in times:
            adj[u].append((v,w))
        
        pq = []
        heapq.heappush(pq, (0, k))

        while pq:
            cost, node = heapq.heappop(pq)

            if node in visit:
                continue

            visit.add(node)

            ans = max(ans, cost)
            for nei, wei in adj[node]: 
                if nei not in visit:
                    heapq.heappush(pq,(wei+cost, nei))
        
        if len(visit)!=n:
            return -1
        return ans
                    
                    