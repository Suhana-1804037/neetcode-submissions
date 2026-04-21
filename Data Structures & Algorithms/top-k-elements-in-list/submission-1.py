class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        for i in nums:
            if i not in mp:
                mp[i]= 0
            mp[i] +=1
        buckets = [[] for _ in range(len(nums)+1)]
        for num, freq in mp.items():
            buckets[freq].append(num)

        res = []
        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res