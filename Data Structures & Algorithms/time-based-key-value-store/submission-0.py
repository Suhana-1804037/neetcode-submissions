class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        #key, value, timestamp = ["alice", "happy", 1]
        if key not in self.store:
            self.store[key]=[]

        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        ans = ""
        point = self.store.get(key, [])

        l, r = 0, len(point)-1
        while l<=r:
            m = (l+r)//2
            if point[m][1]<=timestamp:
                ans = point[m][0]
                l = m+1
            else:
                r = m-1
        return ans
