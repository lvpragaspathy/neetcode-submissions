#from datetime import datetime as dt

class TimeMap:

    def __init__(self):
        self.keys = defaultdict(lambda: defaultdict(int))

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keys[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:

        i = timestamp
        while i >= 0:
            if self.keys[key][i]:
                return self.keys[key][i]
            i -= 1

        return ""
