class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def func(i, cur, total):
            if total==target:
                ans.append(cur.copy())
                return
            if i>=len(nums) or total>target:
                return
            cur.append(nums[i])
            func(i, cur, total+nums[i])
            cur.pop()
            func(i+1, cur, total)
        func(0, [], 0)
        return ans