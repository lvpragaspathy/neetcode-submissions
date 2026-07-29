
from functools import cache as c
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        @c
        def dp(i, money):
            if i > len(nums)-1:
                return money

            return max(dp(i+2, money + nums[i]), dp(i+1, money))

        return dp(0, 0)
            
            
