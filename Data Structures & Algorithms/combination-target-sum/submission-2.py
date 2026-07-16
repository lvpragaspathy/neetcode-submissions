class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = []
        nums.sort()
        
        def backtrack(selected: List[int], curr_sum, i):
            if curr_sum == target:
                combinations.append(selected.copy())
                return
            
            for j in range(i, len(nums)):
                if curr_sum + nums[j] > target:
                    break
                
                selected.append(nums[j])
                backtrack(selected, curr_sum + nums[j], j)
                selected.pop()

        backtrack([], 0, 0)

        return combinations