class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        mxArea = 0
        stack = []

        for i , h in enumerate(heights):
            start = i
            while stack and stack[-1][1]>h:
                idx, hei = stack.pop()
                mxArea = max(mxArea, hei*(i-idx))
                start = idx
            stack.append((start, h))
        
        for i, h in stack:
            mxArea = max(mxArea, h*(len(heights)-i))
        return mxArea