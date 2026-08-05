class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []

        if len(nums) == 1:
            return [[], [nums[0]]]

        out = []

        def backtrack(i, curr_subset):
            if i == len(nums):
                out.append(curr_subset[:])
                return

            curr_subset.append(nums[i])
            backtrack(i + 1, curr_subset)
            curr_subset.pop()
            backtrack(i + 1, curr_subset)

        backtrack(0, [])

        return out
            





