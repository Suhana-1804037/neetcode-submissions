class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        mp = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        ans = []

        def solve(i, curr):
            if i==len(digits):
                ans.append(curr)
                return
            st = mp[digits[i]]
            for j in range(len(st)):
                solve(i+1, curr+st[j])

        solve(0, "")
        return ans