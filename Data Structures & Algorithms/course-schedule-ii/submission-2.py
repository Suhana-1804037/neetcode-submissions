class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans, visit, visited = [], set(), set()

        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        def dfs(crs):
            if crs in visit:
                return False
            if crs in visited:
                return True
            visit.add(crs)
            for i in preMap[crs]:
                if not dfs(i):
                    return False
            visit.remove(crs)
            visited.add(crs)
            ans.append(crs)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return ans