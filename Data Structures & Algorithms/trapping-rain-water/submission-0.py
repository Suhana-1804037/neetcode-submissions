class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        
        l, r = 0, len(height)-1
        mxL, mxR = height[l], height[r]
        while l<r:
            if mxL<=mxR:
                l+=1
                mxL =  max(mxL, height[l])
                ans+= mxL-height[l]
            else:
                r-=1
                mxR = max(mxR, height[r])
                ans+= mxR-height[r]

        return ans
            