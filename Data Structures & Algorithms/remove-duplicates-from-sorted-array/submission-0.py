class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp = []
        k = 0
        temp.append(nums[0])

        for i in range(1, len(nums)):
            if nums[i] > temp[k]:
                temp.append(nums[i])
                k += 1

        for i in range(len(temp)):
            nums[i] = temp[i]
            
        return k + 1
        