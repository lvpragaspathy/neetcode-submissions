class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        productofnums = 1
        for num in nums:
            productofnums *= num

        print(productofnums)

        if productofnums == 0:
            skippedzero = 1
            numzeroes = 0
            for num in nums:
                if num == 0:
                    numzeroes += 1
                else:
                    skippedzero *= num
                
                if numzeroes > 1:
                    print('bailed out')
                    return [0] * len(nums)
            for i in range(len(nums)):
                if nums[i] == 0:
                    output.append(skippedzero)
                else:
                    output.append(0)
            return output
                
            


        output = [productofnums // i for i in nums]

        return output
        