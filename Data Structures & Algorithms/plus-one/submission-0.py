class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = []
        rem = 1
        for i in range(len(digits)-1, -1, -1): #from back
            p = digits[i]+rem
            rem = 1 if p>9 else 0
            ans.append(p%10)
        if rem ==1:
            ans.append(1)
        ans = ans[::-1]
        return ans