class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        
        ans = 0
        def check(x, y):
            if x>=0 and y<n and s[x]!=s[y]: return 0
            val = 0
            
            while x>=0 and y<n and s[x]==s[y]:
                val+=1
                x-=1
                y+=1
            return val
        
        for i in range(n):
            oddCheck = check(i, i)
            evenCheck = check(i, i+1)

            ans +=oddCheck + evenCheck
        return ans