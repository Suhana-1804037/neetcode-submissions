class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        save = [-1]*len(cost)

        def solve(i):
            if i>=len(cost):
                return 0
            if save[i]!=-1:
                return save[i]
            save[i] =  cost[i] + min(solve(i+1), solve(i+2))
            return save[i]
        return min(solve(0), solve(1))