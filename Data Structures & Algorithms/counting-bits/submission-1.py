class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]*(n+1)
        
        p = 1
        for i in range(1, n+1):
            if p*2==i:
                p = i
            ans[i] = 1+ans[i-p]
        return ans