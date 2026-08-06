class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car = []
        for i, num in enumerate(position):
            val = (target - num)/speed[i]
            car.append([num, val])
                
        car.sort(reverse=True)
        ans = 1
        last = car[0][1]
        for i in range(1, len(car)):
            if last<car[i][1]:
                ans+=1
                last = car[i][1]
        return ans
            

            