class Solution:
    from collections import deque
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque() 

        for i in range(0, k):
            window.append(nums[i])

        max_window = []
        max_window.append(max(window))

        for i in range(k, len(nums)):
            window.popleft()
            window.append(nums[i])
            max_window.append(max(window))
        
        return max_window
        