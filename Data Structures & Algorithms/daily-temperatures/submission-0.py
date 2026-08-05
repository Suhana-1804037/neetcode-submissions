class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        for i, val in enumerate(temperatures):
            if i==0:
                stack.append([val, i])
                continue
            if stack[-1][0]>=val:
                stack.append([val, i])
            else:
                while stack and stack[-1][0]<val:
                    valu, ind = stack[-1]
                    ans[ind] = i-ind
                    stack.pop()
                stack.append([val, i])
            
        return ans
            
            
