# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#        nums.sort()
#        n = len(nums)
#        res = []

#        for i in enumerate(nums):
#             if i>0 and nums[i]==nums[i-1]: 
#                 continue
            
#             l, r = i+1, n-1

#             while l<r:
#                 sums = nums[i] + nums[l] + nums[r]

#                 if sums>0:
#                     r-=1
#                 elif sums<0:
#                     l+=1
#                 else:
#                     res.append([nums[i], nums[l], nums[r]])
#                     l+=1;
#                     while nums[l]==nums[l-1] and l<r:
#                         l+=1
#         return res
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i, a in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, n - 1

            while l < r:
                sums = nums[i] + nums[l] + nums[r]

                if sums > 0:
                    r -= 1
                elif sums < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res