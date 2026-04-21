class Solution:
    def count(self, mid: int, piles: List[int], h: int)->bool:
        cal = 0
        for i in piles:
            cal+= ((i+mid-1)//mid)
        return cal <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, hi = 1, max(piles);
        ans = hi
        while l<=hi:
            mid = (l+hi)//2
            if self.count(mid, piles, h):
                ans = mid
                hi = mid - 1
            else:
                l = mid + 1
        
        return ans
