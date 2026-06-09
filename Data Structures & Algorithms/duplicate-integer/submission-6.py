class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        while len(nums) > 1:
            num = nums[0]
            print(nums, " ", num)
            try:
                nums.remove(num)
                print(num)
                nums.remove(num)
                return(True)
            except ValueError:
                pass
        return(False)

        