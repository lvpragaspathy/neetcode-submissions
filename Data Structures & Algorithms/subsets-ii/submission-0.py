class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        
        if len(nums) == 1:
            return [[], nums]

        nums.sort()
        powset = []
        seen = set()

        for mask in range(1 << len(nums)):
            subset = []

            for i , num in enumerate(nums):
                if mask & (1 << i):
                    subset.append(num)

            if tuple(subset) not in seen:
                powset.append(subset)
                seen.add(tuple(subset))

        return powset