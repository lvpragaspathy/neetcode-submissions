from functools import cache

class Solution:
    def climbStairs(self, n: int) -> int:

        @cache
        def helper(steps_remaining):
            if steps_remaining == 0:
                return 1

            if steps_remaining < 0:
                return 0


            return helper(steps_remaining-1) + helper(steps_remaining-2)

        return helper(n)
            
            
        
        