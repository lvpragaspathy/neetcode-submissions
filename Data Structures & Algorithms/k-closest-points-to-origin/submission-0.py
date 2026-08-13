class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x, y): # returns distace form origin
            return math.sqrt((x ** 2) + (y ** 2))
        
        heap = []
        for i in range(len(points)):
            x, y = points[i][0], points[i][1]
            heapq.heappush(heap, (distance(x, y), i))

        out = []
        for i in range(k):
            out.append(points[heapq.heappop(heap)[1]])

        return out
        
        

        
        

