class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        size = len(nums)
        i = 0

        while i < size:
            if nums[i] == val:
                nums.remove(val)
                size = size - 1
            else:
                i = i + 1 
        
        return len(nums)
                