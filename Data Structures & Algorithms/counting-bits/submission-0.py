class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        
        for i in range(n+1):
            a = 0
            for j in range(i+1):
                if (1<<j) & i:
                    a+=1
            ans.append(a)
        return ans