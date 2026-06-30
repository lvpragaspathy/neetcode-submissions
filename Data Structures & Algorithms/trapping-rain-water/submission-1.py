class Solution:
    def trap(self, height: List[int]) -> int:
        prefixes = [-1] * len(height)
        suffixes = [-1] * len(height)

        #calculate prefixes
        premax = 0
        for i, val in enumerate(height):
            prefixes[i] = premax
            if val > premax:
                premax = val

        #calculate suffixes
        sufmax = 0
        for i in range(len(height)-1, -1, -1):
            suffixes[i] = sufmax
            if height[i] > sufmax:
                sufmax = height[i]

        def volAtIndex(i, prefixes, suffixes, height):
            return min(prefixes[i], suffixes[i]) - height[i]

        res = 0
        for i in range(len(height)):
            vol_at_i = max(volAtIndex(i, prefixes, suffixes, height), 0)
            res += vol_at_i
        
        return res



        


            

            

        