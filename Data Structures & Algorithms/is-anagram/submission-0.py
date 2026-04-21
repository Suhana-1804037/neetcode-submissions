class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sSort = sorted(s)
        tSort = sorted(t)

        if sSort==tSort:
            return True
        else:
            return False