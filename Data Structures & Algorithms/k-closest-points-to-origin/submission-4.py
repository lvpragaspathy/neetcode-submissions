class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x, y): # returns distace form origin
            return math.sqrt((x ** 2) + (y ** 2))
        
        heap = []
        for i, point in enumerate(points):
            heapq.heappush_max(heap, (distance(point[0], point[1]), i))
            if len(heap) > k:
                heapq.heappop_max(heap)
            
        return [points[heapq.heappop_max(heap)[1]] for _ in range(k)]
        
        

        
        

