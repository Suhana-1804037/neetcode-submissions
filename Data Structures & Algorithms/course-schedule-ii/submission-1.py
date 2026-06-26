class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans, visit = [], set()
        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        def dfs(crs):
            if crs in visit:
                return False
            if preMap[crs]==[]:
                if crs not in ans:
                    ans.append(crs)
                return True

            visit.add(crs)
            for i in preMap[crs]:
                if not dfs(i):
                    return False
                
            visit.remove(crs)
            preMap[crs]=[]
            ans.append(crs)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return ans