class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        x, ans = 0, 0
        for i in range(len(gas)):
            x+=gas[i]-cost[i]
            if x<0:
                x=0
                ans=i+1
        
        return ans