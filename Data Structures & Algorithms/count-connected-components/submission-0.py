class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit, ans = set(), 0
        
        adj = {i: [] for i in range(n)}
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node, parent):
            if node in visit:
                return
            
            visit.add(node)
            for i in adj[node]:
                if i==parent:
                    continue
                dfs(i, node)
            return
        

        for i in range(n):
            if i not in visit:
                dfs(i, -1)
                ans+=1
        return ans