class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, k-1

        max_window = []
        
        while r < len(nums):
            window = sorted(nums[l:r+1])
            max_window.append(window[-1])

            l += 1
            r += 1
        
        return max_window
        