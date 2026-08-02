class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        val = prices[0]
        for i in range(1, len(prices)):
            if prices[i]<val:
                val = prices[i]
            ans = max(ans, prices[i]-val)
        return ans