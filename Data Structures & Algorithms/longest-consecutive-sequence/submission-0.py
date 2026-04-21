class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = set(nums)
        res = 0
        ans = 0
        for i in nums:
            if i-1 not in mp:
                ans = 0
                while (i+ans) in mp:
                    ans +=1
                res = max(res, ans)

        return res
            