from collections import deque
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.record = deque()

        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.record.remove(key)
            self.record.append(key)
            return self.cache[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache: 
            self.cache[key] = value
            self.record.remove(key)
            self.record.append(key)
        else:
            self.cache[key] = value
            self.record.append(key)
            
            if len(self.cache) > self.capacity:
                x = self.record.popleft()
                self.cache.pop(x)
