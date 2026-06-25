class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = set()
        nums.sort()

        for i in range(len(nums)):
            target = -nums[i] # so that i + j  + k = 0 -> -i (target) = j + k
            l = i + 1 # j 
            r = len(nums) - 1 # k

            while l < r:
                if nums[l] + nums[r] == target:
                    output.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1

        return [list(triplet) for triplet in output]
                  

                    

            
        
            


       
            



        return output
        