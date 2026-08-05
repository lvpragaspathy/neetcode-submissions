class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]

        permutate = []
        usage = [False] * len(nums)

        def backtrack(curr):
            if len(curr) == len(nums):
                permutate.append(curr.copy())

            for i in range(len(nums)):
                if not usage[i]:
                    curr.append(nums[i])
                    usage[i] = True
                    backtrack(curr)
                    curr.pop()
                    usage[i] = False

        backtrack([])
        return permutate


            
            
                
            


            

