class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def func(i, curr):
            if i>=len(nums):
                ans.append(curr.copy())
                return
            for j in range(len(nums)):
                if nums[j] in curr:
                    continue
                curr.append(nums[j])
                func(i+1, curr)
                curr.pop()


        for i in range(len(nums)):
            curr = []
            curr.append(nums[i])
            func(1, curr)
        return ans