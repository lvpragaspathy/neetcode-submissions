from functools import cache

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # we'll start at i = -1 and say cost at -1 is 0 to move to either 0 or 1. 
        n = len(cost)

        @cache
        def dp(i: int) -> int:
            if i == -1:
                return min(dp(i+1), dp(i+2))

            if i >= n:
                return 0

            return cost[i] + min(dp(i+1), dp(i+2))
                   

        return dp(-1)
            

