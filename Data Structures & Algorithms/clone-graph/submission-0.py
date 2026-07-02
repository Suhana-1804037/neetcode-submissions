"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        preMp = {}

        def dfs(dfsNode):
            if dfsNode in preMp:
                return preMp[dfsNode]
            
            copy = Node(dfsNode.val)
            preMp[dfsNode] = copy

            for i in dfsNode.neighbors:
                copy.neighbors.append(dfs(i))
            return copy
        return dfs(node) if node else None