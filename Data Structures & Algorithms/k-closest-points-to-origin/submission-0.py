class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for i, j in points:
            dist = i**2 + j**2
            minHeap.append([dist, i, j])

        heapq.heapify(minHeap)
        ans = []
        while k>0:
           dist, x, y =  heapq.heappop(minHeap)
           ans.append([x, y])
           k-=1
        return ans
