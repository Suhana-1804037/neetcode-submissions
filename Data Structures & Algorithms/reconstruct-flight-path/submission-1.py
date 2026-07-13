class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {i :[] for i, v in (tickets)}
        tickets.sort()
        for u, v in tickets:
            adj[u].append(v)
        
        ans = ["JFK"]

        def dfs(node):
            if len(ans)==len(tickets)+1:
                return True
            if node not in adj:
                return False

            temp = list(adj[node])
            for i, v in enumerate(temp):
                adj[node].pop(i)
                ans.append(v)
                if dfs(v):
                    return True
                adj[node].insert(i, v)
                ans.pop()
            return False

        dfs("JFK")
        return ans