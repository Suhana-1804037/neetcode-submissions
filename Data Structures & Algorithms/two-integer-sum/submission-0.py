class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i, x in enumerate(nums):
            sub = target - x
            if sub in mp:
                return [mp[sub], i]
            mp[x] = i
        return []
            



        