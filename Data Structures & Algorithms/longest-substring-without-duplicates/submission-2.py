class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        setT =  {}
        l, ans = 0,0
        for i in range(len(s)):
            if s[i] in setT:
                l = max(setT[s[i]]+1, l)
            setT[s[i]] = i
            ans = max(ans, i-l+1)
        
        return ans
