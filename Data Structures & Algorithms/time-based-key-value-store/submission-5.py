#from datetime import datetime as dt

class TimeMap:

    def __init__(self):
        self.keys = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keys[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not self.keys[key]:
            return ""


        l, r = 0, len(self.keys[key]) -1 

        while l <= r:
            
            mid = (l+r) // 2
            if self.keys[key][mid][0] == timestamp:
                return self.keys[key][mid][1]

            elif self.keys[key][mid][0] < timestamp:
                l = mid+1
            
            else:
                 r = mid-1

        return self.keys[key][r][1] if r >= 0 else ""
