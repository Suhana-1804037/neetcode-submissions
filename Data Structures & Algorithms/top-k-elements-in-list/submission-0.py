class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        for i in nums:
            if i not in mp:
                mp[i]= 0
            mp[i] +=1
        mp = sorted(mp.items(), key=lambda x: x[1], reverse=True)
        ans = []
        for i in mp[:k]:
            ans.append(i[0])
        return ans
