class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        ans = []
        part=[]

        def solve(i):
            if i>=len(s):
                ans.append(part.copy())
                return
            for j in range(i, len(s)):
                if self.checkPali(s, i, j):
                    part.append(s[i:j+1])
                    solve(j+1)
                    part.pop()

        solve(0)
        return ans
   
    def checkPali(self, st, l, r):
        if len(st)==1:
            return True
        while l<=r:
            if st[l]==st[r]:
                l+=1
                r-=1
            else:
                return False
        return True
        
    
