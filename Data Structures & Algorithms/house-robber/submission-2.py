
from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        @cache
        def dp(i):
            if i > len(nums)-1:
                return 0

            return  max(dp(i+2) + nums[i] , dp(i+1))

        return dp(0)
            
            
