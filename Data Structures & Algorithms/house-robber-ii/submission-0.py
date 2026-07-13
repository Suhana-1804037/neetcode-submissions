class Solution:
    def rob(self, nums: List[int]) -> int:
        
        return max(nums[0], self.solve(nums[1:]), self.solve(nums[:-1]))
    
    def solve(self, num):

        rob1, rob2 = 0, 0
        for i in num:
            newrob = max(rob1+i, rob2 )
            rob1 = rob2
            rob2 = newrob
        return rob2