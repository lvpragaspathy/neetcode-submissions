from functools import cache

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        i = -1
        # well say cost at -1 is 0 to move to either 0 or 1. 
        n = len(cost)

        price = 0 

        @cache
        def dp(i: int, price: int) -> int:
            if i == -1:
                return min(dp(i+1, price), dp(i+2, price))

            if i >= n:
                return price

            return min(dp(i+1, price + cost[i]), dp(i+2, price + cost[i]))
                   

        return dp(-1, 0)
            

