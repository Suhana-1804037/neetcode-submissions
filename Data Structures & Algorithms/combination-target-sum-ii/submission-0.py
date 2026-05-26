class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        def func(i, curr, total):
            if total==target:
                ans.append(curr.copy())
                return
            if i>=len(candidates) or total>target:
                return
            curr.append(candidates[i])
            func(i+1, curr, total+candidates[i])
            curr.pop()
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
                
            func(i+1, curr, total)
            return 
        
        func(0, [], 0)
        return ans