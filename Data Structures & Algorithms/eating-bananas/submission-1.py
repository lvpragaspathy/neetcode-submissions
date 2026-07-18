class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l < r:
            mid = (r + l) // 2
            time = 0

            for pile in piles:
                time += math.ceil(pile / mid)

            if time <= h: 
                r = mid
            else: 
                l = mid + 1

        return r
        


            
                
 
        