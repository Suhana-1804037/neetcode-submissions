class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp ={}

        def dfs(i, val):
            if i>=len(prices):
                return 0
            if (i, val) in dp:
                return dp[(i, val)]
            
            cooldown = dfs(i+1, val)
            
            if val:
                buy = dfs(i+1, not val) - prices[i]
                dp[(i, val)] = max(buy, cooldown)
            else:
                sell =dfs(i+2, not val)+prices[i]
                dp[(i, val)] = max(sell, cooldown)
            return dp[(i, val)]
              
        return dfs(0, True)
            