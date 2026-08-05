class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []

        if len(nums) == 1:
            return [[], nums]
        
        powset = []

        for mask in range(1 << len(nums)):
            subset = []

            for i, num in enumerate(nums):
                if mask & (1 << i):
                    subset.append(num)

            powset.append(subset)

        return powset
            





