class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        anslen, ans = 1, 0
        n = len(s)
        p, leng, stinx = 1, 1, 1
        for i in range(n):
            p, stinx = 1, i
            #even check
            if i+1<n and s[i]==s[i+1] :
                leng = 2
                while i-p>=0 and i+1+p<n and s[i-p]==s[i+1+p]:
                    leng+=2
                    stinx = i-p
                    p+=1
            if anslen<leng:
                anslen = leng
                ans = stinx
            if i+1<n and i-1>=0 and s[i-1]==s[i+1]: #odd check
                leng, p = 1, 1
                while (i-p>=0 and i+p<n and s[i-p]==s[i+p]):
                    leng+=2
                    stinx = i-p
                    p+=1
            if anslen<leng:
                anslen = leng
                ans = stinx
        return s[ans : ans + anslen]
