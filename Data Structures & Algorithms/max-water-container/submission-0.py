class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right, ans  = 0, len(heights)-1, 0

        while left<right:
            ans = max(ans ,(right-left) * min(heights[left], heights[right]))

            if heights[right]>=heights[left]:
                left+=1
            else:
                right-=1
        return ans