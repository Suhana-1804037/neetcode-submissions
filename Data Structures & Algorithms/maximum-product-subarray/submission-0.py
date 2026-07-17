class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = max(nums)
        curMin, curMax = 1, 1

        for i in nums:
            if i==0:
                curMin, curMax = 1, 1
                continue
            tmp = i*curMax
            curMax = max(i*curMax, i*curMin, i)
            curMin = min(i*curMin, tmp, i )
            ans = max(ans, curMax)
        return ans
            